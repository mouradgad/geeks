class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        current=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        count=(count//2)+1
        temp=0
        while head!=None:
            temp+=1
            if count==temp:
                return head.data
            head=head.next
