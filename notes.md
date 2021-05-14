# 数据结构

```
Union find和Trie肯定是要会的，binary index tree和segment tree正常情况下尽量选一种掌握应该也就够了，
不过segment tree比binary index tree适用范围更广，但是真用到的地方并不那么多。
suffix array和k-d tree知道有这么个玩意大概能干啥也就够了吧。真考到就只能认了，这个太难掌握了
sparse table的话知道是binary lifting这种办法，可以实现range minimum query就差不多了，其实不难。
从难易程度来看的话，binary index tree/ segment tree/ sparse table都属于已有知识掌握比较好的情况下学习难度不是特别大的数据结构（当然不包括什么进阶用法的情况下）。
segment tree比binary index tree适用范围更广，面试中能用到的主要就是可以求任意区间极值，而binary index tree只能算prefix的极值。
像动态插入删除节点，通过懒标记实现区间查询更改这种操作真考到只能认了（我也只是知道有这么个操作，并不会实现）。
kd-tree和suffix array难度就要进阶一些了。而且细节又多。
个人建议，如果基础的数据结构和算法没有掌握好的话，先把基础打牢。
然后不会union find和 Trie的话一定花时间先把这两个数据结构掌握。
再之后可以线段树和Fenwick（binary index tree）选一个去掌握。Fenwick代码量短，运行速度快，线段树更好理解，但是代码长。
再之后sparse table可以尝试去掌握一下RMQ和倍增（binary lifting）的思路，力扣的kth ancestor这个题目和RMQ思路很接近。而且之前G家考过binary lifting优化的dp。
suffix array和kd-tree个人感觉除非是闲得难受，学有余力，否则就不管了吧
```

# BFS

## BFS的使用场景

1. 分层遍历(简单图的边长均为x的最短路径)
2. 连通块问题()
3. 拓补排序(比DFS简单)
4. 求所有方案问题

---

# 分治法

分治法适合解决同类型问题(排序、找大小(二分法))

参考merge sort，分治法我更喜欢叫divide and merge

## 分治法和二分的区别

二分之处理一半，而分治法两边都要处理

## 分治法适合什么数据结构

连续数组、二叉树、矩阵(Matrix)，链表很勉强，寻址太慢了

## 二叉树的高度O(h)

假设元素个数是n，高度最好情况是O(logn)(平衡二叉树)，高度最坏情况是O(n)每层就一个节点

所以综上所述，用O(h)表示二叉树的高度

## 节点数量为n的二叉树有几个不同的子树？

答案是n个，以某点为根将它所有子节点囊括进去，所以有多少个节点就有多少个子树

# HashMap

所谓O(1)时间复杂度其实是有先决条件的，更准确说是O(size of key)的时间复杂度

输入key经过Hash Function后得到一个正整数的下标，通过下标找到内部的bucket数组的索引位置

同样的key能保证算出的结果是一样的，但是不保证不同的key算出的index会一样，哈希冲突

冲突的解决方法1: Open hashing，开哈希【业界常用，面试准备】

哈希内部数组的每个格子是一个链表，但是链表内包含key和value，算出来相同的Hash的key,value都挤在一起，都在一个链表上

冲突的解决方法2: Closed Hashing

如果数组格子被占了(联想茅厕被占)，则后来者往后一格(或者有其它挪动算法)，缺点是删除元素后，要将格子标记为deleted，代表曾经有人过

下次搜索冲突的值时，遇到deleted也不会停，会继续往下一格搜索

总结哈希冲突的解决方案:

1. open_hashing(开散列法): 哈希表所基于的数组中每个位置都是一个LinkedList的头结点。这样冲突的(key, value) pair都放在同一个链表中
2. closed_hash(闭散列法): 发生冲突时，后来的元素往下一个位置去找空位

[open hashing的动画演示](https://cs.usfca.edu/~galles/visualization/OpenHash.html)

记录冲突链表中的元素顺序其实是没有关系的，所以新冲突的(key, value)pair都是插入到头结点后，这样就不用记录尾节点的指针

例如 Head->1中插入3(会插入到Head和1之间)  =>  Head->3->1

所以开散列法实际上可以存的元素是无穷个，但哈希表如果冲突严重，那就需要哈希扩容

所以链表内用到什么数据结构，更准确的回答是: 数组+(单/双)链表+红黑树，红黑树的扩容性能更佳

所有编程语言自带的堆的删除操作都是O(n)，只有值不重复而且有HashMap索引才能删得快

像Rust的BinaryHeap除了pop就没有直接删除的操作，只有retain也要遍历一遍才能删除

堆找到要删的元素要O(n)，然后把堆的最后元素覆盖到被删节点，然后sift_down

## 为什么(非内存)数据库索引要用B+树

B+树实际上是一种多叉树，降低了树的深度

## Skip List(跳跃表)有序链表?

## 双向宽度优先搜索的优化多少时间复杂度?

答案是√n而不是1/2，实际上除2除的是指数，最佳优化效果下情况下k^n -> k^(n/2)