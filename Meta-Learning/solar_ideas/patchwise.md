현재 코드는 **전체 이미지(full image)를 하나의 샘플로 사용**하여 태스크를 구성하고 있습니다.

### 현재 코드의 동작 방식 (Full Image-wise)

`MetaSolarPredictionDataset`의 `__getitem__` 메서드를 살펴보면 명확히 알 수 있습니다.

```python
# meta_dataset.py의 __getitem__ 일부

def __getitem__(self, idx):
    # 1. 전체 데이터셋에서 랜덤 인덱스를 샘플링
    indices = random.sample(range(len(self.dataset)), self.k_shot + self.k_query)
    
    support_indices = indices[:self.k_shot]
    query_indices = indices[self.k_shot:]

    # 2. 해당 인덱스의 (입력 시퀀스, 타겟 시퀀스) 쌍을 가져옴
    #    이때 self.dataset[i]는 SolarPredictionDataset에서 정의한 대로
    #    (input_len, H, W) 크기의 전체 이미지 시퀀스를 반환함
    support_x, support_y = [], []
    for i in support_indices:
        x, y = self.dataset[i] # x, y는 전체 이미지 시퀀스
        support_x.append(x)
        support_y.append(y)
    
    # ... (이하 동일) ...
```

이 방식은 다음과 같이 동작합니다.

1.  **태스크 정의**: 하나의 태스크는 **서로 다른 시간대의 전체 이미지 시퀀스들**의 집합으로 정의됩니다. 예를 들어, 한 태스크의 서포트 셋은 (2021-01-01의 시퀀스, 2021-03-15의 시퀀스, 2022-07-20의 시퀀스, ...) 와 같이 구성될 수 있습니다.
2.  **학습 목표**: 모델은 다양한 날짜와 시간에 걸친 거시적인 기상 패턴의 변화에 적응하는 법을 학습하게 됩니다. 예를 들어, '맑은 날' 패턴과 '흐린 날' 패턴 사이를 빠르게 전환하는 능력을 배울 수 있습니다.

이 방식도 의미가 있지만, 논문에서 언급했던 **"다양한 지역(various regions)에 대한 일반화"**나 **"국지적인 미기후(micro-climate)에 대한 적응력 강화"**라는 목표를 달성하기 위해서는 패치 단위 학습이 더 적합합니다.

---

### 패치 단위(Patch-wise) 학습을 적용하려면?

패치 단위 학습을 적용하려면 `MetaSolarPredictionDataset`을 수정하여, 태스크를 **'특정 지역(패치)에서의 시계열 예측'** 문제로 재정의해야 합니다.

#### 패치 단위 학습의 개념

1.  **태스크 재정의**: 하나의 태스크는 **하나의 고정된 공간적 위치(패치)에서 추출한 시간적 시퀀스**로 정의됩니다.
    *   **태스크 1**: (0,0) 위치에서 잘라낸 패치들의 시간 시퀀스.
    *   **태스크 2**: (0,64) 위치에서 잘라낸 패치들의 시간 시퀀스.
    *   ... 등등.
2.  **학습 목표**: 모델은 각기 다른 지리적 특성(내륙, 해안, 산악 등)을 가진 패치들에 빠르게 적응하는 법을 학습합니다. 이를 통해 MAML의 핵심 목표인 **공간적 일반화(spatial generalization)** 능력을 키울 수 있습니다.

#### 패치 단위 학습을 위한 코드 수정 방향

`MetaSolarPredictionDataset`을 다음과 같이 수정해야 합니다.

1.  **`__init__`**:
    *   전체 이미지 크기(H, W)와 패치 크기(patch_size), 스트라이드(stride)를 인자로 받습니다.
    *   가능한 모든 패치의 시작 위치 `(y, x)`를 미리 계산하여 리스트(`self.patch_locations`)로 저장합니다. 이 리스트의 각 요소가 하나의 잠재적인 태스크가 됩니다.

2.  **`__len__`**:
    *   `tasks_per_epoch` 대신, `len(self.patch_locations)`를 반환하도록 하여 에포크마다 모든 패치를 한 번씩 보도록 할 수 있습니다. (또는 기존처럼 `tasks_per_epoch`를 유지하고 랜덤 샘플링도 가능)

3.  **`__getitem__`**:
    *   `idx`를 사용하여 `self.patch_locations`에서 패치 위치 `(y, x)`를 선택합니다. 이것이 현재 태스크의 "지역"이 됩니다.
    *   전체 `SolarPredictionDataset`에서 `k_shot + k_query`개의 **시간적 시퀀스**를 랜덤하게 샘플링합니다.
    *   샘플링된 각 시퀀스(전체 이미지)에서, 선택된 위치 `(y, x)`에 해당하는 **패치**를 잘라냅니다.
    *   잘라낸 패치들로 서포트 셋과 쿼리 셋을 구성하여 반환합니다.

**수정된 `MetaSolarPredictionDataset` (의사 코드):**

```python
class MetaSolarPatchDataset(Dataset):
    def __init__(self, dataset, patch_size, stride, tasks_per_epoch, k_shot, k_query):
        self.dataset = dataset # SolarPredictionDataset 인스턴스
        self.patch_size = patch_size
        self.stride = stride
        self.tasks_per_epoch = tasks_per_epoch
        self.k_shot = k_shot
        self.k_query = k_query

        # 전체 이미지 크기 가져오기 (예시)
        img_c, img_h, img_w = self.dataset[0][0].shape
        
        # 가능한 모든 패치 위치 계산
        self.patch_locations = []
        for y in range(0, img_h - patch_size + 1, stride):
            for x in range(0, img_w - patch_size + 1, stride):
                self.patch_locations.append((y, x))

    def __len__(self):
        return self.tasks_per_epoch

    def __getitem__(self, idx):
        # 1. 태스크(지역)를 랜덤하게 선택
        patch_y, patch_x = random.choice(self.patch_locations)

        # 2. 해당 지역의 시간적 데이터를 샘플링
        time_indices = random.sample(range(len(self.dataset)), self.k_shot + self.k_query)
        
        support_x_patches, support_y_patches = [], []
        query_x_patches, query_y_patches = [], []

        # 3. 전체 이미지에서 패치를 잘라내어 태스크 데이터 구성
        for i in time_indices[:self.k_shot]:
            full_x, full_y = self.dataset[i]
            # 패치 자르기: [C, H, W] -> [C, patch_size, patch_size]
            patch_x = full_x[:, patch_y:patch_y+self.patch_size, patch_x:patch_x+self.patch_size]
            patch_y_ = full_y[:, patch_y:patch_y+self.patch_size, patch_x:patch_x+self.patch_size]
            support_x_patches.append(patch_x)
            support_y_patches.append(patch_y_)

        # (쿼리 셋에 대해서도 동일하게 반복)
        # ...

        return torch.stack(support_x_patches), torch.stack(support_y_patches), \
               torch.stack(query_x_patches), torch.stack(query_y_patches)
```

**결론:** 현재 코드는 패치 단위 학습이 아니며, 이를 적용하려면 데이터셋 클래스(`MetaSolarPredictionDataset`)를 수정하여 **태스크의 정의를 '시간의 변화'에서 '공간의 변화'로 바꾸는 작업**이 필요합니다.
