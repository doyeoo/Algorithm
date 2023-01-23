import sys

size, num = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(arr)

def merge_sort(arr) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q = (p + r)/2;       # q는 p, r의 중간 지점
        merge_sort(arr, p, q);      # 전반부 정렬
        merge_sort(arr, q + 1, r);  # 후반부 정렬
        merge(arr, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(arr, p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (arr[i] ≤ arr[j])
        then tmp[t++] <- arr[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- ArithmeticError[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- arr[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- arr[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        arr[i++] <- tmp[t++]; 
}