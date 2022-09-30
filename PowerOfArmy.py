test_cases = int(input())
emp = []
if 1 <= test_cases <= 100:
    for i in range(test_cases):
        total_elements = int(input())
        if 2 <= total_elements <= 1000:
            ele_listed = map(int, input().split())
            ele_listed = list(ele_listed)
            if total_elements == len(ele_listed):
                eleMax = max(ele_listed)
                eleMin = min(ele_listed)
                emp.append(str(int(eleMax) - int(eleMin)))
                if i == test_cases-1:
                    for k in emp:
                        print(k)
