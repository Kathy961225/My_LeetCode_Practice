http://www.cnblogs.com/TenosDoIt/p/3387000.html

https://blog.csdn.net/u014450222/article/details/83002321

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        relation = {} # relation tuples
        new_prev = None
        cur = head
        while cur != None:
            new_list = Node(None, None, None)
            new_list.val = cur.val
            relation[cur] = new_list
            if new_prev:
                new_prev.next = new_list
            new_prev = new_list
            cur = cur.next
        for key,value in relation.iteritems():
            if key.random != None:
                value.random = relation[key.random]
        new_head = relation[head] if head else None
        return new_head

https://blog.csdn.net/u014450222/article/details/83002321
class Solution {
 
public:
 
    RandomListNode *copyRandomList(RandomListNode *head) {
 
        if(head==NULL)
 
            return NULL;
 
        //先复制每一个节点，如原来是1->2->3->4,复制后变为1->1'->2->2'->3->3'->4->4'
 
        RandomListNode *p=head;
 
        while(p){
 
            RandomListNode *tmp=new RandomListNode(p->label);
 
            tmp->next=p->next;
 
            p->next=tmp;
 
            p=p->next->next;//走两步，跨过新加入的节点     
 
        }
 
        //复制Random指针
 
        p=head;
 
        RandomListNode *q=head->next;
 
        while(p){
 
            if(p->random)
 
            q->random=p->random->next;
 
            p=p->next->next;//注意，此处要走两步
 
            if(q->next)
 
            q=q->next->next;//注意，此处要走两步
 
        }
 
        //分离两个链表：即分为1->2->3->4和1'->2'->3'->4'
 
        p=head;
 
        q=head->next;
 
        RandomListNode *newHead=q;
 
        RandomListNode *tmp1=NULL;
 
        RandomListNode *tmp2=NULL;
 
         
 
        while(p){
 
            tmp1=p->next->next;
 
            if(q->next==NULL)
 
                break;//1->1'的情况在此退出（链表遍历到最后两个节点时也从此处退出）
 
            tmp2=q->next->next;//此处：链表至少有4个节点1->1'->2->2'
 
            p->next=tmp1;
 
            q->next=tmp2;
 
            p=p->next;
 
            q=q->next;
 
            tmp1=tmp1->next->next;//链表至少有4个节点1->1'->2->2'，所以可以保证tmp1往后移动一次
 
            if(tmp2->next)
 
                tmp2=tmp2->next->next;
 
            else
 
                tmp2=NULL;//即tmp2已经是链表最后一个节点，此时会在下次一进入while时，从break处退出（q->next==NULL）
 
        }
 
        p->next=NULL;
 
        return newHead;
 
    }
 
};



class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        //
        if(!head) return head;
        RandomListNode* p=head;
        while(p){
            RandomListNode* node=new RandomListNode(p->label);
            node->next=p->next;
            p->next=node;
            p=node->next;    
        }
        p=head;
        while(p){
            p->next->random=p->random?p->random->next:NULL;//千年老bug，不容易重视：不能保证p->random存在，就要添加保护措施，不能“裸奔”
            p=p->next->next;    
        }

        RandomListNode* newhead=head->next;

        p=head->next;
        while(p){//把新旧链表分开，旧链表重新组装成原来的样子，而不是随意扔掉！

            head->next=p->next;
            head=head->next;
            p->next=head?head->next:NULL;//千年老bug，不容易重视：不能保证head存在，就要添加保护措施，不能“裸奔”
            p=p->next;  
        }
        return newhead;
    }
};


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
 
        if not head:
            return None
        if head.next == None:
            return Node(head.val, head.next, head.random)
        
        old = head
        
        while old:
            new = Node(old.val, None, None)
            new.next = old.next
            old.next = new
            old = old.next.next
        
        old = head
        new = head.next
        while old:
            if old.random:
                new.random = old.random.next
                old = old.next.next
            if new.next:
                new = new.next.next
                
        new = head.next
        
        temp = head.next
        
        while temp:
            head.next = temp.next
            head = head.next
            if head:
                temp.next = head.next
            else:
                temp.next = None
            temp = temp.next
            
        return new


https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution