length_of_circular_linked_list = int(input())

circular_linked_list = list(map(int,input().strip().split(" ")))

final_list = [circular_linked_list[i] for i in range(3)]
for i in circular_linked_list:
    if i not in final_list:
        final_list.append(i)
print(len(final_list))
for i in final_list:
    print(i,end=" ")
