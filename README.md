Leetcode
========

TODO:

43/415 字符串整数相乘/相加

415是经典面试题利用字符串模拟竖式加法进行大数相加

有兴趣但是困难级别的题: 1. 推箱子 2. 华容道

有意思的但是没有找到题号的问题:

1. 海盗分金币问题(比较脑筋急转弯的递推)
2. 最大直方图矩阵(Longest Histgram Rectangle), 单调栈O(n^3)->O(n)

因为leetcode-cn上我多做了一些面试题/剑指5OFFER题(其实是重复的题目)，所以我leetcode国服账户会比全球服账户多AC了29题

表格中没有代码文件链接的都是过于简单30秒就能搞定的题

| # | Title | Solutions | Category |
|---| ----- | -------- | ---------- |
|1|[Two Sum](https://leetcode.com/problems/two-sum/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/btree_map_two_sum.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/collections/two_sum_test.go), [Java](https://github.com/pymongo/java_leetcode/blob/master/src/test/java/com/leetcode/collections/HashMapTwoSum.java)|btree_map, bitwise(two_s_complement)|
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Python](linked_list/add_two_numbers.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/add_two_linked_list.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/collections/traverse_two_list_node_test.go), [Java](https://github.com/pymongo/java_leetcode/blob/master/src/test/java/com/leetcode/collections/TraverseTwoListNode.java)|create/traverse_list_node|
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)|[Python](string/longest_non_repeated_substr.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/string/longest_non_repeated_substr.rs)|sliding_window|
|4|[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)|[Python](binary_search/median_of_two_sorted_arrays.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/binary_search/median_of_two_sorted_arrays.rs)|binary_search|
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|[Python](palindrome/longest_palindromic_substr.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/string/longest_palindromic_substr.rs)|multi_solutions, manacher, suffix_array|
|6|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|[Python](string/zigzag_conversion.py)||
|7|[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|[Python](easy/reverse_integer.py)||
|8|[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|[Python](easy/string_to_integer_atoi.py)||
|9|[Palindromic Number](https://leetcode.com/problems/palindrome-number/)|[Python](palindrome/longest_palindromic_substr.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/i32_is_palindromic.rs))|half_traverse_i32|
|10|[Regular Expression Matching](https://leetcode.coms/problem/regular-expression-matching/)|[Python](dp/regular_expression_matching.py)||
|11|[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)|[Python](two_sum_two_pointers/container_with_most_water.py)||
|12|[Integer to Roman](https://leetcode.com/problems/integer-to-roman/)|[Python](easy/int_to_roman.py)||
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|[Python](easy/int_to_roman.py)||
|14|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|[Python](divide_conquer/longest_common_prefix_of_k_strs.py)||
|15|[3Sum](https://leetcode.com/problems/3sum/)|[Python](two_sum_two_pointers/three_sum_plans_detail.py)|two_pointers, two_sum|
|16|[3Sum Closest](https://leetcode.com/problems/3sum-closest/)|[Python](two_sum_two_pointers/three_sum_closest.py)|two_sum|
|17|[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|[Python](dfs_perm_comb/phone_9_keypad_combination.py)|product(笛卡尔积)|
|18|[4Sum](https://leetcode.com/problems/4sum/)|[Python](two_sum_two_pointers/four_sum_plans_detail.py)|two_pointers, two_sum|
|19|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Python](linked_list/remove_nth_node_from_end.py)|sliding_window|
|20|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|[Python](collections/valid_parentheses.py)|stack|
|21|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|[Python](divide_conquer/merge_k_sorted_lists.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/merge_two_sorted_linked_list.rs)||
|22|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|[Python](dfs_perm_comb/generate_parentheses.py)|回溯穷举|
|23|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)|[Python](divide_conquer/merge_k_sorted_lists.py)||
|24|[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/swap_nodes_in_pairs.rs)||
|26|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|[Python](partition_array/move_zeros.py)||
|27|[Subarray Sum](https://lintcode.com/problem/remove-element/)|[Python](partition_array/move_zeros.py)||
|28|[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/string/contains_substr_kmp.rs), [Python](string/find_substr.py)|kmp, dfa, multi_solutions|
|31|[Next Permutation](https://leetcode.com/problems/next-permutation/)|[Python](dfs_perm_comb/next_permutation.py)||
|33|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|[Python](binary_search/rotated_sorted_array_search.py)|binary_search|
|34|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)|[Python](binary_search/binary_search_first_and_last.py)|binary_search|
|35|[Search Insert Position](https://leetcode.com/problems/search-insert-position/)|[Python](binary_search/search_insert_position.py)||
|36|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)|[Python](dfs_perm_comb/valid_soduku.py)||
|37|[Soduku Solver](https://leetcode.com/problems/soduku-solver/)|[Python](dfs_perm_comb/soduku_solver.py)||
|39|[Combination Sum](https://leetcode.com/problems/combination-sum/)|[Python](dfs_perm_comb/combination_target_sum.py)||
|44|[Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)|[Python](dp/wildcard_matching.py)||
|46|[Permutations](https://leetcode.com/problems/permutations/)|[Python](dfs_perm_comb/permutation.py)|backtracking|
|47|[Permutations II](https://leetcode.com/problems/permutations-ii/)|[Python](dfs_perm_comb/permutation.py)|backtracking|
|49|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|[Python](collections/group_anagrams.py)||
|50|[Pow(x, n)](https://leetcode.com/problems/powx-n/)|[Python](math/pow.py)|binary_search, 快速幂运算|
|51|[N Queens](https://leetcode.com/problems/n-queens)|[Python](dfs_perm_comb/n_queens.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/backtracking/n_queens.py)||
|52|[N Queens II](https://leetcode.com/problems/n-queens-ii)|[Python](dfs_perm_comb/n_queens.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/backtracking/n_queens.py)||
|53|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[Python](greedy/maximum_subarray.py)|greedy, dp|
|55|[Jump Game](https://leetcode.com/problems/jump-game/)|[Python](dp/jump_game.py)|greedy, dp|
|60|[Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)|[Python](dfs_perm_comb/permutation.py)||
|62|[Unique Paths](https://leetcode.com/problems/unique-paths/)|[Python](dfs_perm_comb/unique_paths.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/unique_path.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/permutation/shortest_paths_on_checkerboard_test.go)|combination|
|63|[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)|[Python](dp/unique_paths_2.py)||
|64|[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)|[Python](easy/grid_min_path_sum.py)||
|66|[Plus One](https://leetcode.com/problems/plus-one/)|[Python](easy/plus_one.py)||
|67|[Add Binary](https://lintcode.com/problem/add-binary/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/add_bigint_string.cpp)||
|69|[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|[Python](math/sqrt.py)|牛顿连续均值求根法|
|70|[Climb Stairs](https://leetcode.com/problems/climbing-stairs/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/tail_recursion_fibonacci.rs)|tail_recursion, fibonacci|
|72|[Edit Distance](https://leetcode.com/problems/edit-distance/)|[Python](dp/edit_distance.py)||
|73|[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/set_matrix_zeroes.rs)||
|74|[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)|[Python](binary_search/search_a_2d_matrix.py)||
|75|[Sort Colors](https://leetcode.com/problems/sort-colors/)|[Python](partition_array/sort_colors.py)|three_pointers, partition_array|
|77|[Combinations](https://leetcode.com/problems/combinartions/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/backtracking/combinations.rs), [C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/n_ary_tree_level_order.cpp)||
|78|[Subsets](https://leetcode.com/problems/subsets/)|[Python](dfs_perm_comb/subsets_combinations.py)||
|79|[Word Search](https://leetcode.com/problems/word-search/)|[Python](dfs_perm_comb/word_search.py)||
|81|[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)|[Python](binary_search/rotated_sorted_array_search_2_with_duplicate.py)|binary_search|
|82|[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/linked_list/remove_duplicates_from_sorted_list.cpp)||
|83|[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/linked_list/remove_duplicates_from_sorted_list.cpp)||
|88|[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/merge_two_sorted_arrays.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/sorting/merge_two_sorted_arrays_test.go), [Python](divide_conquer/merge_two_sorted_arrays.py)|merge_sort|
|89|[Gray Code](https://leetcode.com/problems/gray-code/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/gray_code.rs), [Python](easy/gray_code.py)||
|90|[Subsets](https://leetcode.com/problems/subsets-ii/)|[Python](dfs_perm_comb/subsets_combinations.py)||
|91|[Decode Ways](https://leetcode.com/problems/decode-ways/)|[Python](dp/decode_ways.py)||
|92|[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/reverse_linked_list.rs), [Python](linked_list/reverse_linked_list.py)||
|94|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|98|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|[Python](binary_tree/bst_valid.py)||
|99|[Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/description)|[Python](binary_tree/bst_recover_swap_two_nodes.py)||
|102|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|[Python](binary_tree/traversal_level_order.py)|BFS|
|104|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[Python](binary_tree/depth_max_min.py)||
|105|[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|[Python](binary_tree/construct_from_pre_order_and_in_order.py)|DFS, stack|
|106|[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|[Python](binary_tree/construct_from_in_order_and_post_order.py)|DFS|
|107|[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)|[Python](binary_tree/traversal_level_order.py)|BFS|
|110|[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)|[Python](binary_tree/depth_is_balance_binary_tree.py)|divide_and_conquer|
|111|[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[Python](binary_tree/depth_max_min.py)|divide_and_conquer, BFS|
|114|[Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|[Python](binary_tree/in_place_flatten_binary_tree_to_linked_list.py)||
|118|[Pascals Triangle](https://leetcode.com/problems/pascals-triangle/)|[Python](easy/pascals_triangle.py)||
|119|[Pascals Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)|[Python](easy/pascals_triangle.py)||
|120|[Triangle](https://leetcode.com/problems/triangle/)|[Python](dp/triangle.py)||
|121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|[Python](dp/stock.py)||
|122|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|[Python](dp/stock.py)||
|123|[Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)|[Python](dp/stock.py)||
|124|[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|[Python](binary_tree/binary_tree_maximum_path_sum.py)||
|125|[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|[Python](palindrome/valid_palindrome.py)|two_pointers|
|126|[Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)|[Python](bfs/word_ladder_2.py)|BFS+DFS|
|127|[Word Ladder](https://leetcode.com/problems/word-ladder/)|[Python](bfs/word_ladder.py)|双向BFS|
|128|[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|[Python](collections/longest_consecutive_sequence.py)|并查集|
|133|[Clone Graph](https://leetcode.com/problems/clone-graphs/)|[Python](graph/clone_graph.py)|DFS, BFS|
|134|[Gas Station](https://leetcode.com/problems/gas-station/)|[Python](greedy/gas_station.py)|greedy|
|136|[Single Number](https://leetcode.com/problems/single-number/)|[Python](bitwise/xor_find_single.py)||
|138|[Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)|[Python](graph/clone_linked_list_with_random_ptr.py)||
|139|[Word Break](https://leetcode.com/problems/word-break/)|[Python](dp/backpack_4_word_break_coin_change.py)|完全背包问题|
|140|[Word Break II](https://leetcode.com/problems/word-break-ii/)|[Python](dp/word_break_2.py)||
|141|[Linked List Cycle](https://lintcode.com/problem/linked-list-cycle/)|[Python](linked_list/linked_list_cycle.py)||
|142|[Linked List Cycle II](https://lintcode.com/problem/linked-list-cycle-ii/)|[Python](linked_list/linked_list_cycle.py)||
|144|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|145|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|145|[LRU Cache](https://leetcode.com/problems/lru-cache/)|[Python](linked_list/lru_cache.py)|double_linked_list, OrderedDict|
|151|[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)|[Python](rotate_reverse_circle_shift/reverse_words_in_a_string.py)||
|153|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)|[Python](binary_search/rotated_sorted_array_search.py)|binary_search|
|154|[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)|[Python](binary_search/rotated_sorted_array_min_2_with_duplicate.py)|binary_search|
|155|[Min Stack](https://leetcode.com/problems/min-stack/)|[Python](collections/min_stack.py)||
|160|[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)|[Python](linked_list/linked_list_cycle.py)||
|167|[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|[Python](two_sum_two_pointers/two_sum_2_input_is_sorted.py)|two_pointers|
|169|[Majority Element](https://leetcode.com/problems/majority-element/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/majority-element.rs)||
|170_LOCK|[Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)|[Python](two_sum_two_pointers/two_sum_3_impl.py)|two_pointers|
|172|[Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)|[Python](factorization/factorial_trailing_zeroes.py)|factorial|
|173|[Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)|[Python](binary_tree/bst_in_order_iterator.py)||
|175|[Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)|||
|176|[Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)|[SQL](database_problems/second_highest_salary.sql)||
|181|[Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)|||
|182|[Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)|[SQL](database_problems/duplicate_emails.sql)||
|183|[Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)|||
|188|[Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)|[Python](dp/stock.py)||
|189|[Rotate Array](http://leetcode.com/problems/rotate-array/)|[Python](rotate_reverse_circle_shift/rotate_array_right_circle_shift_elements.py)|reverse, circle_shift|
|190|[Reverse Bits](https://leetcode.com/problems/reverse-bits/)|[Python](bitwise/number_of_1_bits.py)||
|191|[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)|[Python](bitwise/number_of_1_bits.py)||
|198|[House Robber](https://leetcode.com/problems/house-robber/)|[Python](dp/house_robber.py)||
|200|[Number of Islands](https://leetcode.com/problems/number-of-islands/)|[Python](graph/number_of_islands.py)|union_find, DFS, BFS|
|202|[Happy Number](https://leetcode.com/problems/happy-number/)|[Python](easy/happy_number.py)||
|206|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|[Python](linked_list/reverse_linked_list.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/reverse_linked_list.rs)||
|208|[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)|[Python](tire/impl_tire_prefix_tree.py)|前缀树/字典树|
|207|[Course Schedule](https://leetcode.com/problems/course-schedule/)|[Python](graph/course_schedule_2.py)|BFS, topological_sorting|
|209|[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)|[Python](two_sum_two_pointers/minimun_size_subarray_sum.py)|sliding_window|
|210|[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)|[Python](graph/course_schedule_2.py)|BFS, topological_sorting|
|212|[Word Search II](https://leetcode.com/problems/word-search-ii/)|[Python](dfs_perm_comb/word_search_2.py)|前缀树|
|213|[House Robber II](https://leetcode.com/problems/house-robber-ii/)|[Python](dp/house_robber.py)||
|215|[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)|[Python](sorting_and_query/quick_select_kth_largest.py)|quick_select, quick_sort, heap|
|217|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|||
|219|[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/contains_duplicate_2.rs)||
|225|[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|[Python](collections/impl_stack_by_queue.py)||
|226|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)|[Python](easy/invert_binary_tree.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/reverse_linked_list.rs)||
|227|[Basic Calculator II](https://leetcode.com/problems/basic-calculator/)|[Python](brain_twists/calculator_2.py)||
|230|[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|231|[Power of Two](https://leetcode.com/problems/power-of-two/)|[Python](bitwise/is_power_of_2.py)|bitwise, dichotomy|
|232|[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|[Python](collections/impl_stack_by_queue.py)||
|234|[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/linked_list_is_palindrome.rs)||
|235|[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)|[Python](binary_tree/bst_lowest_common_ancestor.py)||
|236|[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|[Python](binary_tree/binary_tree_lowest_common_ancestor.py)|divide_and_conquer|
|237|[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)|[Python](easy/delete_node_in_a_linked_list.py)||
|240|[Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)|[Python](binary_search/search_a_2d_matrix_2.py)||
|242|[Valid Anagram](https://leetcode.com/problems/valid-anagram/)|[Python](collections/valid_anagram.py)||
|257|[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|[Python](binary_tree/root_to_leaf_paths_find_all.py)|DFS, backtracking|
|263|[Ugly Number](https://leetcode.com/problems/ugly-number/)|[Python](easy/ugly_number.py)||
|264|[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)|[Python](unclassified/ugly_number_2_nth_ugly.py)||
|266_LOCK|[Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)|[Python](palindrome/palindrome_permutation.py)|greedy|
|269_LOCK|[Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)|[Python](graph/alien_dictionary.py)|heapq, topological_sorting|
|270_LOCK|[Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)|[Python](binary_tree/bst_closest_value.py)||
|272_LOCK|[Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)|[Python](binary_tree/bst_closest_value_2.py)||
|278|[First Bad Version](https://leetcode.com/problems/first-bad-version/)|[Python](binary_search/first_bad_version.py)|partition_array|
|279|[Perfect Squares](https://leetcode.com/problems/perfect-squares/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|283|[Move Zeros](https://leetcode.com/problems/move-zeroes/)|[Python](partition_array/move_zeros.py)|partition_array, 快慢双指针|
|287|[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)|[Python](brain_twists/find_duplicate_number.py)|快慢双指针|
|290|[Word Pattern](https://leetcode.com/problems/word-pattern/)|[Python](easy/word_pattern.py)||
|291_LOCK|[Word Pattern II](https://leetcode.com/problems/word-pattern-ii/)|[Python](dfs_perm_comb/word_pattern_2.py)|DFS|
|292|[Nim Game](https://leetcode.com/problems/nim-game/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/nim_game.rs)||
|297|[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)|[Python](binary_tree/binary_tree.py)|serialize|
|300|[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)|[Python](dp/longest_increase_subsequence.py)|接龙型动态规划|
|302_LOCK|[Smallest Rectangle Enclosing Black Pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels)|[Python](binary_search/smallest_rectangle_enclosing_black_pixels.py)||
|303|[Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)|[Python](easy/range_sum_query_immutable.py)||
|307|[Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)|[Python](segment_tree/segment_tree_range_sum.py)||
|309|[Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)|[Python](dp/stock.py)||
|311_LOCK|[Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/)|[Python](math/sparse_matrix_multiplication.py)||
|312|[Burst Balloons](https://leetcode.com/problems/burst-balloons/)|[Python](dp/burst_ballon.py)||
|322|[Coin Change](https://leetcode.com/problem/coin-change/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|326|[Power of Three](https://leetcode.com/problems/power-of-three/)|[Python](bitwise/is_power_of_3.py)|bitwise|
|337|[House Robber III](https://leetcode.com/problems/house-robber-iii/)|[Python](dp/house_robber.py)||
|342|[Power of Four](https://leetcode.com/problems/power-of-four/)|[Python](bitwise/is_power_of_4.py)|bitwise|
|343|[Integer Break](https://leetcode.com/problems/integer-break/)|[Python](dp/integer_break.py)|划分类DP|
|344|[Reverse Array](https://leetcode.com/problems/reverse-string/)|[Python](rotate_reverse_circle_shift/reverse_string.py)||
|347|[Top K Frequent Elements](https://leetcode.com/problems/reverse-string/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/priority_queue/top_k_frequent_elements.rs)||
|349|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|350|[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|354|[Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)|[Python](dp/russian_doll_envelopes.py)||
|367|[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)|[Python](math/sqrt.py)||
|368|[Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)|[Python](dp/largest_divisible_subset.py)||
|369_LOCK|[Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/)|[Python](linked_list/bottom_up_plus_one_linked_list.py)||
|371|[Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)|[Python](bitwise/binary_addition.py)|binary_addition|
|377|[Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|380|[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)|[Python](collections/insert_delete_get_random_o1.py)||
|381|[Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)|[Python](collections/insert_delete_get_random_o1.py)||
|409|[Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)|[Python](palindrome/longest_palindromic_combination.py)|dp(greedy)|
|412|[Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)|[Python](easy/fizz_buzz.py)||
|413|[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|[Python](easy/reverse_integer.py)||
|415|[Add String](https://leetcode.com/problems/add-strings/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/add_bigint_string.cpp)||
|416|[Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)|[Python](dp/backpack_1_2.py)|0-1背包问题|
|426|[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)|[Python](two_sum_two_pointers/longest_repeating_character_replacement.py)||
|429|[N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/n_ary_tree_level_order.cpp)||
|449|[Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)|[Python](binary_tree/bst_serialize.py)|DFS, stack|
|454|[4Sum II](https://leetcode.com/problems/4sum-ii/)|[Python](two_sum_two_pointers/four_sum_2.py)|two_sum|
|461|[Number of 1 Bits](https://leetcode.com/problems/hamming-distance/)|[Python](bitwise/number_of_1_bits.py)||
|474|[Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)|[Python](dp/backpack_ones_and_zeros.py)|完全背包问题|
|490_LOCK|[The Maze](https://leetcode.com/problems/the-maze/)|[Python](bfs/the_maze.py)||
|494|[Target Sum](https://leetcode.com/problems/target-sum/)|[Python](dp/backpack_1_target_sum.py)|0-1背包问题|
|498|[Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/)|[Python](unclassified/diagonal_traverse.py)||
|503|[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/monotonic_stack/next_greater_element_2.rs)||
|507|[Perfect Number](https://leetcode.com/problems/perfect-number/)|[Python](factorization/perfect_number.py)||
|509|[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/tail_recursion_fibonacci.rs)|tail_recursion, fibonacci|
|518|[Coin Change 2](https://leetcode.com/problem/coin-change-2/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|535|[Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/)|||
|536_LOCK|[Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string/)|[Python](binary_tree/construct_from_string_with_parentheses.py)||
|547|[Friend Circles](https://leetcode.com/problems/friend-circles/)|[Python](graph/friend_circles.py)|union_find, BFS, BFS|
|559|[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/n_ary_tree_level_order.cpp)||
|567|[Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/reverse_words_in_a_string_3.cpp)||
|589|[N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)|[Python](easy/n_ary_tree_preorder_postorder.py)||
|590|[N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)|[Python](easy/n_ary_tree_preorder_postorder.py)||
|595|[Big Countries](https://leetcode.com/problems/big-countries/)|||
|606|[Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)|[Python](binary_tree/construct_from_string_with_parentheses.py)||
|617|[Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)|[Python](binary_tree/merge_two_binary_tree.py)||
|620|[Not Boring Movies](https://leetcode.com/problems/not-boring-movies/)|||
|625_LOCK|[Minimum Factorization](https://leetcode.com/problems/minimum-factorization/)|[Python](factorization/minimum_factorization.py)|greedy|
|627|[Swap Salary](https://leetcode-cn.com/problems/swap-salary/)|[SQL](database_problems/invert_sex.sql)||
|633|[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)|[Python](binary_tree/traversal_level_order.py)||
|650|[2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/)|[Python](brain_twists/copy_paste_times.py)||
|653|[First Unique Number in Data Stream](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)|[Python](binary_tree/bst_two_sum.py)||
|658|[Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)|[Python](binary_search/find_k_closest_elements.py)|binary_search|
|669|[Trim A Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)|[Python](binary_tree/bst_trim_in_range.py)||
|674|[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)|[Python](easy/longest_continuous_increase_subsequence.py)||
|680|[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)|[Python](palindrome/valid_palindrome_2.py)|two_pointers, greedy|
|695|[Max Area of Island](https://leetcode.com/problems/max-area-of-island/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/bfs/max_area_of_island.rs)||
|696|[Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/)|[Python](unclassified/count_binary_substring.py)||
|700|[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[Python](binary_tree/bst_search.py)||
|702_LOCK|[Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)|[Python](binary_search/binary_search_unknown_size_sorted_array.py)|binary_search_first, 倍增法|
|703|[Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)|[Python](collections/top_k_largest_stream_min_heap.py)|min_heap|
|704|[Binary Search](https://leetcode.com/problems/binary-search/)|[Python](binary_search/binary_search.py)|binary_search|
|705|[Design HashSet](https://leetcode.com/problems/design-hashset/)|[Python](linked_list/impl_hashmap.py)||
|706|[Design HashMap](https://leetcode.com/problems/design-hashmap/)|[Python](linked_list/impl_hashmap.py)||
|709|[To Lower Case](https://leetcode.com/problems/to-lower-case/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/to_lowercase.rs)||
|714|[Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)|[Python](dp/stock.py)||
|716_LOCK|[Max Stack](https://leetcode.com/problems/max_stack/)|[Python](collections/max_stack.py)||
|760_LOCK|[Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/)|[Python](collections/mapping_two_anagram_list_int.py)||
|796|[Rotate String](https://leetcode.com/problems/rotate-string/)|[Python](rotate_reverse_circle_shift/rotate_string.py)|Rabin-Karp(rolling_hash), kmp|
|743|[Network Delay Time](https://leetcode.com/problems/network-delay-time/)|[Python](bfs/network_delay_time_dijkstra.py)||
|771|[Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)|[Python](easy/jewels_and_stones.py)||
|807|[Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/max_increase_to_keep_city_skyline.rs)||
|841|[Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/keys_and_rooms.cpp)||
|845|[Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/)|[Python](binary_search/mountain_array_longest.py)|mountain_array|
|852|[Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)|[Python](binary_search/mountain_array_max.py)|mountain_array, binary_search|
|861|[Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/)|[Python](greedy/score_after_flipping_matrix.py)|greedy|
|867|[Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/transpose.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/easy/test_transpose_matrix.go), [C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/transpose_matrix.cpp)||
|869|[Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/)|[Python](brain_twists/reordered_power_of_2.py)|permutation|
|875|[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)|[Python](binary_search/koko_eating_bananas.py)||
|876|[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)|[Python](linked_list/middle_of_linked_list.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/middle_of_linked_list.rs)|快慢双指针|
|877_TODO|[Stone Game](https://leetcode.com/problems/stone-game/)|||
|887_TODO|[Super Egg Drop](https://leetcode.com/problems/super-egg-drop)||dp|
|889|[Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)|[Python](binary_tree/construct_from_pre_order_and_post_order.py)|DFS|
|912|[Sort An Array](https://leetcode.com/problems/sort-an-array/)|[Python](sorting_and_query/basic_sorting.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/quick_sort.rs)|multi_solutions|
|941|[Valid Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)|[Python](binary_search/mountain_array_valid.py)|mountain_array|
|953|[Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)|[Python](unclassified/verifying_an_alien_dictionary.py)||
|973|[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)|[Python](sorting_and_query/k_closest_points_to_origin.py)|quick_select, sort_by_multi_keys|
|1046|[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)|[Python](collections/last_stone_weight.py)||
|1049|[Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)|[Python](dp/backpack_1_2.py)|0-1背包问题|
|1095|[Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)|[Python](binary_search/mountain_array_find.py)|binary_search, mountain_array|
|1099_LOCK|[Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/)|[Python](two_sum_two_pointers/two_sum_le_count.py)|two_pointers|
|1108|[Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)|||
|1143|[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|[Python](dp/longest_common_subsequence.py)||
|1147|[Work Plan](https://www.lintcode.com/problem/work-plan/)|[Python](dp/house_robber.py)||
|1167_LOCK|[Longest Common Subsequence](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)|[Python](easy/minimum_cost_to_connect_sticks.py)||
|1213_LOCK|[Intersection of Three Sorted Arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|1226|[The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/concurrency/dining_philosophers_problem.cpp)||
|1227|[Airplane Seat Assignment Probability](https://leetcode.com/problems/airplane-seat-assignment-probability/)|[Python](brain_twists/airplane_seat_assignment_probability.py)||
|1266|[Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/min_time_visiting_all_points.rs)||
|1281|[Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|1295|[Minimum Operations to Make Array Equal](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)|||
|1313|[Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/)|[Python](easy/decompress_run_length_encoded_list.py)||
|1342|[Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)|[Python](easy/number_of_steps_to_reduce_a_number_to_zero.py)||
|1365|[How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)|[Python](easy/how_many_numbers_are_smaller_than_current.py)|前缀和(prefix_sum)|
|1379|[Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)|[Python](easy/find_a_corresponding_node_in_a_cloned_tree.py)||
|1389|[Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/)|[Python](easy/create_target_array_in_the_given_order.py)||
|1395|[Count Number of Teams](https://leetcode.com/problems/count-number-of-teams/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/count_number_of_teams.rs)||
|1429_LOCK|[First Unique Number](https://leetcode.com/problems/first-unique-number/)|[Python](linked_list/first_unique_number_in_stream.py)||
|1431|[Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)|[Python](easy/kids_with_the_greatest_number_of_candies.py)||
|1464|[Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)|||
|1470|[Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)|[Python](easy/shuffle_the_array.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/shuffle_the_array.rs)||
|1476|[Subrectangle Queries](https://leetcode.com/problems/subrectangle-queries/)|[Python](easy/subrectangle_queries.py)||
|1480|[Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)|[Python](easy/running_sum_of_1d_array.py)||
|1486|[XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)|[Python](easy/xor_operation_in_an_array.py)||
|1512|[Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)|[Python](dfs_perm_comb/numbers_of_good_pairs.py)||
|1528|[Shuffle String](https://leetcode.com/problems/shuffle-string/)|[Python](easy/shuffle_string.py)||
|1534|[Count Good Triplets](https://leetcode.com/problems/count-good-triplets/)|||
|1551|[Minimum Operations to Make Array Equal](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/min_operations_to_make_array_equal.rs)||
|1572/5491|[Shuffle String](https://leetcode.com/problems/matrix-diagonal-sum/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/matrix_diagonal_sum.rs)||
|1576/5507|[Replace All ?'s to Avoid Consecutive Repeating Characters](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/)|[Python](easy/replace_question_mark_to_avoid_consecutive_repeating_char.py)||
|1577/5508|[Number of Ways Where Square of Number Is Equal to Product of Two Numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/number_of_ways_where_square_of_number_is_equal_to_product_of_two_numbers.rs)||
|1578/5509|[Minimum Deletion Cost to Avoid Repeating Letters](https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/submissions/)|[Python](easy/minimum_deletion_cost_to_avoid_repeating_letters.py)||

---

剑指Offer
========

忽略LeetCode主站上重复出现的题以及过于简单的剑指Offer题

| # | Title | Solutions | Category |
|---| ----- | -------- | ---------- |
|59|[队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)|[Python](collections/max_queue.py)||
|60|[n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)|[Python](dp/dices_sum.py)||
|61|[扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)|[Python](easy/straight_in_playing_cards.py)||
|62|[圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)|[Python](brain_twists/josephus.py)|约瑟夫环|
|66|[构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof)|[Python](easy/contruct_product_array.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/construct_product_array.rs)||

---

LintCode
========

| # | Title | Solutions | Category |
|---| ----- | -------- | ---------- |
|1|[A + B Problem](https://lintcode.com/problem/a-b-problem/)|[Python](bitwise/binary_addition.py)|binary_addition|
|2|[Trailing Zeros](https://lintcode.com/problem/trailing-zeros/)|[Python](factorization/factorial_trailing_zeroes.py)|factorial|
|3|[Digit Counts](https://lintcode.com/problem/digit-counts/)|[Python](unclassified/digits_count.py)||
|4|[Ugly Number II](https://lintcode.com/problem/ugly-number-ii/)|[Python](unclassified/ugly_number_2_nth_ugly.py)||
|5|[Kth Largest Element](https://lintcode.com/problem/kth-largest-element/)|[Python](sorting_and_query/quick_select_kth_largest.py)|quick_select, quick_sort, heap|
|6|[Merge Two Sorted Arrays](https://lintcode.com/problem/merge-two-sorted-arrays/)|[Python](divide_conquer/merge_two_sorted_arrays.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/merge_two_sorted_linked_list.rs)|merge_sort|
|7|[Serialize and Deserialize Binary Tree](https://lintcode.com/problem/serialize-and-deserialize-binary-tree/)|[Python](binary_tree/binary_tree.py)|serialize|
|8|[Rotate String](https://lintcode.com/problem/rotate-string/)|[Python](rotate_reverse_circle_shift/rotate_string.py)|Rabin-Karp|
|9|[Fizz Buzz](https://lintcode.com/problem/fizz-buzz/)|[Python](easy/fizz_buzz.py)||
|10|[String Permutation II](https://lintcode.com/problem/string-permutation-ii/)|[Python](dfs_perm_comb/permutation.py)|backtracking|
|11|[Search Range in Binary Search Tree](https://lintcode.com/problem/search-range-in-binary-search-tree/)|[Python](binary_tree/bst_search.py)||
|12|[Min Stack](https://lintcode.com/problem/min-stack/)|[Python](collections/min_stack.py)||
|13|[Implement strStr()](https://lintcode.com/problem/implement-strstr/)|[Python](string/find_substr.py)|kmp, Rabin-Karp(rolling_hash)|
|14|[First Position of Target](https://lintcode.com/problem/first-position-of-target/)|[Python](binary_search/binary_search_first_and_last.py)|binary_search|
|15|[Permutations](https://lintcode.com/problem/permutations/)|[Python](dfs_perm_comb/permutation.py)|backtracking|
|16|[Permutations II](https://lintcode.com/problem/permutations-ii/)|[Python](dfs_perm_comb/permutation.py)|backtracking|
|17|[Subsets](https://lintcode.com/problem/subsets/)|[Python](dfs_perm_comb/subsets_combinations.py)||
|18|[Subsets II](https://lintcode.com/problem/subsets-ii/)|[Python](dfs_perm_comb/subsets_combinations.py)||
|20|[Dices Sum](https://lintcode.com/problem/dices-sum/)|[Python](dp/dices_sum.py)||
|22|[Flatten List](https://lintcode.com/problem/flatten-list/)|[Python](easy/flatten_list.py)||
|28|[Search a 2D Matrix](https://lintcode.com/problem/search-a-2d-matrix/)|[Python](binary_search/search_a_2d_matrix.py)||
|31|[Partition Array](https://lintcode.com/problem/partition-array/)|[Python](partition_array/partition_array.py)|two_pointers|
|33|[N Queens](https://lintcode.com/problem/n-queens)|[Python](dfs_perm_comb/n_queens.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/backtracking/n_queens.py)||
|34|[N Queens II](https://lintcode.com/problem/n-queens-ii)|[Python](dfs_perm_comb/n_queens.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/backtracking/n_queens.py)||
|35|[Reverse Linked List](https://lintcode.com/problem/reverse-linked-list/)|[Python](linked_list/reverse_linked_list.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/reverse_linked_list.rs)||
|36|[Reverse Linked List II](https://lintcode.com/problem/reverse-linked-list-ii/)|[Python](linked_list/reverse_linked_list.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/reverse_linked_list_2.rs)||
|37|[Reverse 3-digit Integer](https://lintcode.com/problem/reverse-3-digit-integer/)|||
|38|[Search a 2D Matrix II](https://lintcode.com/problem/search-a-2d-matrix-ii/)|[Python](binary_search/search_a_2d_matrix_2.py)||
|40|[Implement Queue by Two Stacks](https://lintcode.com/problem/implement-queue-by-two-stacks/)|[Python](collections/impl_queue_by_stack.py)||
|41|[Maximum Subarray](https://lintcode.com/problem/maximum-subarray/)|[Python](greedy/maximum_subarray.py)|greedy, dp|
|46|[Majority Element](https://lintcode.com/problem/majority-element/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/majority-element.rs)||
|49|[Sort Letters by Case](https://lintcode.com/problem/sort-letters-by-case/)|[Python](partition_array/partition_array_by_odd_and_even.py)||
|50|[Product of Array Exclude Itself](https://lintcode.com/problem/product-of-array-exclude-itself/)|[Python](easy/contruct_product_array.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/construct_product_array.rs)||
|52|[Next Permutation](https://lintcode.com/problem/next-permutation/)|[Python](dfs_perm_comb/next_permutation.py)||
|53|[Reverse Words in a String](https://lintcode.com/problem/reverse-words-in-a-string/)|[Python](rotate_reverse_circle_shift/reverse_words_in_a_string.py)||
|56|[Two Sum](https://lintcode.com/problem/two-sum/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/btree_map_two_sum.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/collections/two_sum_test.go), [Java](https://github.com/pymongo/java_leetcode/blob/master/src/test/java/com/leetcode/collections/HashMapTwoSum.java)|btree_map, bitwise(two_s_complement)|
|57|[3Sum](https://lintcode.com/problem/3sum/)|[Python](two_sum_two_pointers/three_sum_plans_detail.py)|two_pointers, two_sum|
|58|[4Sum](https://lintcode.com/problem/4sum/)|[Python](two_sum_two_pointers/four_sum_plans_detail.py)|two_pointers, two_sum|
|59|[3Sum Closest](https://lintcode.com/problem/3sum-closest/)|[Python](two_sum_two_pointers/three_sum_closest.py)|two_sum|
|60|[Search Insert Position](https://lintcode.com/problem/search-insert-position/)|[Python](binary_search/search_insert_position.py)||
|61|[Search for a Range](https://lintcode.com/problem/search-for-a-range/)|[Python](binary_search/binary_search_first_and_last.py)||
|62|[Search in Rotated Sorted Array](https://lintcode.com/problem/search-in-rotated-sorted-array/)|[Python](binary_search/rotated_sorted_array_search.py)|binary_search|
|63|[Search in Rotated Sorted Array II](https://lintcode.com/problem/search-in-rotated-sorted-array-ii/)|[Python](binary_search/rotated_sorted_array_search_2_with_duplicate.py)|binary_search|
|64|[Merge Sorted Array](https://lintcode.com/problem/merge-sorted-array/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/merge_two_sorted_arrays.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/sorting/merge_two_sorted_arrays_test.go), [Python](divide_conquer/merge_two_sorted_arrays.py)|merge_sort|
|65|[Median of Two Sorted Arrays](https://lintcode.com/problem/median-of-two-sorted-arrays/)|[Python](binary_search/median_of_two_sorted_arrays.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/binary_search/median_of_two_sorted_arrays.rs)|binary_search|
|66|[Binary Tree Preorder Traversal](https://lintcode.com/problem/binary-tree-preorder-traversal/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|67|[Binary Tree Inorder Traversal](https://lintcode.com/problem/binary-tree-inorder-traversal/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|68|[Binary Tree Postorder Traversal](https://lintcode.com/problem/binary-tree-postorder-traversal/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|69|[Binary Tree Level Order Traversal](https://lintcode.com/problem/binary-tree-level-order-traversal/)|[Python](binary_tree/traversal_level_order.py)|BFS|
|69|[Binary Tree Level Order Traversal II](https://lintcode.com/problem/binary-tree-level-order-traversal-ii/)|[Python](binary_tree/traversal_level_order.py)|BFS|
|72|[Construct Binary Tree from Inorder and Postorder Traversal](https://lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal/)|[Python](binary_tree/construct_from_in_order_and_post_order.py)|DFS|
|73|[Construct Binary Tree from Preorder and Inorder Traversal](https://lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal/)|[Python](binary_tree/construct_from_pre_order_and_in_order.py)|DFS, stack|
|74|[First Bad Version](https://lintcode.com/problem/first-bad-version/)|[Python](binary_search/first_bad_version.py)|partition_array|
|75|[Find Peak Element](https://lintcode.com/problem/find-peak-element/)|[Python](binary_search/mountain_array_max.py)|mountain_array, binary_search|
|76|[Longest Increasing Subsequence](https://lintcode.com/problem/longest-increasing-subsequence/)|[Python](dp/longest_increase_subsequence.py)|接龙型动态规划|
|77|[Longest Common Subsequence](https://lintcode.com/problem/longest-common-subsequence/)|[Python](dp/longest_common_subsequence.py)||
|78|[Longest Common Prefix](https://lintcode.com/problem/longest-common-prefix/)|[Python](divide_conquer/longest_common_prefix_of_k_strs.py)||
|79|[Longest Common Substring](https://lintcode.com/problem/longest-common-substring/)|[Python](dp/longest_common_substring.py)||
|80|[Median](https://lintcode.com/problem/median/)|[Python](sorting_and_query/quick_select_kth_largest.py)|quick_select|
|86|[Binary Search Tree Iterator](https://lintcode.com/problem/binary-search-tree-iterator/)|[Python](binary_tree/bst_in_order_iterator.py)||
|88|[Lowest Common Ancestor of a Binary Tree](https://lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/)|[Python](binary_tree/binary_tree_lowest_common_ancestor.py)|divide_and_conquer|
|90|[k Sum II](https://lintcode.com/problem/k-sum-ii/)|[Python](dfs_perm_comb/k_sum_2.py)||
|92|[Backpack](https://lintcode.com/problem/backpack/)|[Python](dp/backpack_1_2.py)||
|93|[Balanced Binary Tree](https://lintcode.com/problem/balanced-binary-tree/)|[Python](binary_tree/depth_is_balance_binary_tree.py)|divide_and_conquer|
|94|[Binary Tree Maximum Path Sum](https://lintcode.com/problem/binary-tree-maximum-path-sum/)|[Python](binary_tree/binary_tree_maximum_path_sum.py)||
|95|[Validate Binary Search Tree](https://lintcode.com/problem/validate-binary-search-tree/)|[Python](binary_tree/bst_valid.py)||
|97|[Maximum Depth of Binary Tree](https://lintcode.com/problem/maximum-depth-of-binary-tree/)|[Python](binary_tree/depth_max_min.py)||
|100|[Remove Duplicates from Sorted Array](https://lintcode.com/problem/remove-duplicates-from-sorted-array/)|[Python](partition_array/move_zeros.py)||
|102|[Linked List Cycle](https://lintcode.com/problem/linked-list-cycle/)|[Python](linked_list/linked_list_cycle.py)||
|103|[Linked List Cycle II](https://lintcode.com/problem/linked-list-cycle-ii/)|[Python](linked_list/linked_list_cycle.py)||
|104|[Merge k Sorted Lists](https://lintcode.com/problem/merge-k-sorted-lists/)|[Python](divide_conquer/merge_k_sorted_lists.py)||
|105|[Copy List with Random Pointer](https://lintcode.com/problem/copy-list-with-random-pointer/)|[Python](graph/clone_linked_list_with_random_ptr.py)||
|107|[Word Break](https://lintcode.com/problem/word-break/)|[Python](dp/backpack_4_word_break_coin_change.py)|完全背包问题|
|109|[Triangle](https://lintcode.com/problem/triangle/)|[Python](dp/triangle.py)||
|110|[Minimum Path Sum](https://lintcode.com/problem/minimum-path-sum/)|[Python](easy/grid_min_path_sum.py)||
|112|[Remove Duplicates from Sorted List](https://lintcode.com/problem/remove-duplicates-from-sorted-list/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/linked_list/remove_duplicates_from_sorted_list.cpp)||
|113|[Remove Duplicates from Sorted List II](https://lintcode.com/problem/remove-duplicates-from-sorted-list-ii/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/linked_list/remove_duplicates_from_sorted_list.cpp)||
|114|[Unique Paths](https://lintcode.com/problem/unique-paths/)|[Python](dfs_perm_comb/unique_paths.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/unique_path.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/permutation/shortest_paths_on_checkerboard_test.go)|combination|
|115|[Unique Paths II](https://lintcode.com/problem/unique-paths-ii/)|[Python](dp/unique_paths_2.py)||
|116|[Jump Game](https://lintcode.com/problem/jump-game/)|[Python](dp/jump_game.py)|greedy, dp|
|119|[Edit Distance](https://lintcode.com/problem/edit-distance/)|[Python](dp/edit_distance.py)||
|120|[Word Ladder](https://lintcode.com/problem/word-ladder/)|[Python](bfs/word_ladder.py)|双向BFS|
|121|[Word Ladder II](https://lintcode.com/problem/word-ladder-ii/)|[Python](bfs/word_ladder_2.py)|BFS+DFS|
|123|[Word Search](https://lintcode.com/problem/word-search/)|[Python](dfs_perm_comb/word_search.py)||
|124|[Longest Consecutive Sequence](https://lintcode.com/problem/longest-consecutive-sequence/)|[Python](collections/longest_consecutive_sequence.py)|并查集|
|125|[Backpack II](https://lintcode.com/problem/backpack-ii/)|[Python](dp/backpack_1_2.py)||
|127|[Topological Sorting](https://lintcode.com/problem/topological-sorting/)|[Python](graph/topological_sorting.py)|BFS, topological_sorting|
|128|[Hash Function](https://lintcode.com/problem/hash-function/)|[Python](collections/hash_function.py)||
|129|[Rehashing](https://lintcode.com/problem/rehashing/)|[Python](collections/rehashing.py)||
|132|[Word Search II](https://lintcode.com/problem/word-search-ii/)|[Python](dfs_perm_comb/word_search_2.py)|前缀树|
|134|[LRU Cache](https://lintcode.com/problem/lru-cache/)|[Python](linked_list/lru_cache.py)|double_linked_list, OrderedDict|
|135|[Combination Sum](https://lintcode.com/problem/combination-sum/)|[Python](dfs_perm_comb/combination_target_sum.py)||
|137|[Clone Graph](https://lintcode.com/problem/clone-graphs/)|[Python](graph/clone_graph.py)|DFS, BFS|
|138|[Subarray Sum](https://lintcode.com/problem/subarray-sum/)|[Python](unclassified/subarray_sum_zero.py)||
|140|[Fast Power](https://lintcode.com/problem/fast-power/)|[Python](math/pow.py)|binary_search, 快速幂运算|
|141|[Sqrt(x)](https://lintcode.com/problem/sqrtx/)|[Python](math/sqrt.py)|牛顿连续均值求根法|
|142|[O(1) Check Power of 2](https://lintcode.com/problem/o1-check-power-of-2/)|[Python](bitwise/is_power_of_2.py)|bitwise, dichotomy|
|143|[Sort Colors II](https://lintcode.com/problem/sort-colors-ii/)|[Python](sorting_and_query/sort_colors_2.py)|quick_sort, counting_sort|
|144|[interleaving_positive_and_negative_numbers](https://lintcode.com/problem/sort-colors-ii/)|[Python](partition_array/interleaving_positive_and_negative_numbers.py)||
|145|[Lower case to Uppercase](https://lintcode.com/problem/lowercase-to-uppercase/)|||
|147_LOCK|[Narcissistic Number](https://lintcode.com/problem/narcissistic-number)|[Python](easy/narcissistic_number.py)||
|148|[Sort Colors](https://lintcode.com/problem/sort-colors/)|[Python](partition_array/sort_colors.py)|three_pointers, partition_array|
|149|[Best Time to Buy and Sell Stock](https://lintcode.com/problem/best-time-to-buy-and-sell-stock/)|[Python](dp/stock.py)||
|150|[Best Time to Buy and Sell Stock II](https://lintcode.com/problem/best-time-to-buy-and-sell-stock-ii/)|[Python](dp/stock.py)||
|151|[Best Time to Buy and Sell Stock III](https://lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/)|[Python](dp/stock.py)||
|152|[Combinations](https://lintcode.com/problem/combinartions/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/backtracking/combinations.rs), [C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/n_ary_tree_level_order.cpp)||
|154|[Regular Expression Matching](https://lintcode.com/problem/regular-expression-matching/)|[Python](dp/regular_expression_matching.py)||
|155|[Minimum Depth of Binary Tree](https://lintcode.com/problem/minimum-depth-of-binary-tree/)|[Python](binary_tree/depth_max_min.py)||
|158|[Valid Anagram](https://lintcode.com/problem/valid-anagram/)|[Python](collections/valid_anagram.py)||
|159|[Find Minimum in Rotated Sorted Array](https://lintcode.com/problem/find-minimum-in-rotated-sorted-array/)|[Python](binary_search/rotated_sorted_array_search.py)|binary_search|
|160|[Find Minimum in Rotated Sorted Array II](https://lintcode.com/problem/find-minimum-in-rotated-sorted-array/)|[Python](binary_search/rotated_sorted_array_min_2_with_duplicate.py)|binary_search|
|162|[Set Matrix Zeroes](https://lintcode.com/problem/set-matrix-zeroes/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/set_matrix_zeroes.rs)||
|165|[Merge Two Sorted Lists](https://lintcode.com/problem/merge-two-sorted-lists/)|[Python](divide_conquer/merge_k_sorted_lists.py)||
|167|[Add Two Numbers](https://lintcode.com/problem/add-two-numbers/)|[Python](linked_list/add_two_numbers.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/add_two_linked_list.rs), [Go](https://github.com/pymongo/go_leetcode/blob/master/collections/traverse_two_list_node_test.go), [Java](https://github.com/pymongo/java_leetcode/blob/master/src/test/java/com/leetcode/collections/TraverseTwoListNode.java)|create/traverse_list_node|
|168|[Burst Balloons](https://lintcode.com/problem/burst-balloons/)|[Python](dp/burst_ballon.py)||
|171|[Anagrams](https://lintcode.com/problem/anagrams/)|[Python](collections/group_anagrams.py)||
|172|[Subarray Sum](https://lintcode.com/problem/remove-element/)|[Python](partition_array/move_zeros.py)||
|174|[Remove Nth Node From End of List](https://lintcode.com/problem/remove-nth-node-from-end-of-list/)|[Python](linked_list/remove_nth_node_from_end.py)|sliding_window|
|175|[Invert Binary Tree](https://lintcode.com/problem/invert-binary-tree/)|[Python](easy/invert_binary_tree.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/reverse_linked_list.rs)||
|183|[Wood Cut](https://lintcode.com/problem/wood-cut/)|[Python](binary_search/wood_cut.py)|greedy|   
|187|[Gas Station](https://lintcode.com/problem/gas-station/)|[Python](greedy/gas_station.py)|greedy|
|190|[Next Permutation II](https://lintcode.com/problem/next-permutation-ii/)|[Python](dfs_perm_comb/next_permutation.py)||
|192|[Wildcard Matching](https://lintcode.com/problem/wildcard-matching/)|[Python](dp/wildcard_matching.py)||
|197|[Permutation Index](https://lintcode.com/problem/permutation-index/)|[Python](easy/permutation_index.py)||
|200|[Longest Palindromic Substring](https://lintcode.com/problem/longest-palindromic-substring/)|[Python](palindrome/longest_palindromic_substr.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/string/longest_palindromic_substr.rs)|multi_solutions, manacher, suffix_array|
|221|[String Permutation](https://lintcode.com/problem/string-permutation/)|[Python](collections/valid_anagram.py)||
|224|[String Permutation](https://lintcode.com/problem/string-permutation/)|[Python](collections/valid_anagram.py)|
|228_LOCK|[Middle of the Linked List](https://lintcode.com/problem/middle-of-linked-list/)|[Python](linked_list/middle_of_linked_list.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/middle_of_linked_list.rs)|快慢指针|
|235|[Prime Factorization](https://lintcode.com/problem/prime-factorization/)|[Python](factorization/prime_factorization.py)|分解质因数|
|241_LOCK|[String to Integer (atoi)](https://lintcode.com/problem/string-to-integer-atoi/)|[Python](easy/string_to_integer_atoi.py)||
|249|[Count of Smaller Number before itself](https://lintcode.com/problem/count-of-smaller-number-before-itself/)|[Python](segment_tree/count_of_smaller_number_before_itself.py)|sqrt_n|
|254|[Drop Eggs](https://lintcode.com/problem/drop-eggs/)|[Python](dp/drop_eggs.py)|sqrt_n|
|272_LOCK|[Climbing Stairs II](https://lintcode.com/problem/climbing-stairs-ii/)|[Python](dp/climb_stairs_2.py)||
|283|[Max of 3 Numbers](https://lintcode.com/problem/max-of-3-numbers/)|||
|309|[Interleaved Array](https://lintcode.com/problem/interleaved-array/)|||
|366|[Fibonacci](https://lintcode.com/problem/fibonacci/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/tail_recursion_fibonacci.rs)|tail_recursion, fibonacci|
|372|[Delete Node in a Linked List](https://lintcode.com/problem/delete-node-in-a-linked-list/)|[Python](easy/delete_node_in_a_linked_list.py)||
|373|[Partition Array by Odd and Even](https://lintcode.com/problem/partition-array-by-odd-and-even/)|[Python](partition_array/partition_array_by_odd_and_even.py)||
|376|[Binary Tree Path Sum](https://lintcode.com/problem/binary-tree-path-sum/)|[Python](binary_tree/root_to_leaf_paths_target_sum.py)|DFS, backtracking|
|380|[Intersection of Two Linked Lists](https://lintcode.com/problem/intersection-of-two-linked-lists/)|[Python](linked_list/linked_list_cycle.py)||
|382_LOCK|[Triangle Count](https://lintcode.com/problem/triangle-count/)|[Python](two_sum_two_pointers/triangle_count.py)|two_sum, 双指针|
|383|[Container With Most Water](https://lintcode.com/problem/container-with-most-water/)|[Python](two_sum_two_pointers/container_with_most_water.py)||
|384|[Longest Substring Without Repeating Characters](https://lintcode.com/problem/longest-substring-without-repeating-characters/)|[Python](string/longest_non_repeated_substr.py), [Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/string/longest_non_repeated_substr.rs)|sliding_window|
|386|[Longest Substring with At Most K Distinct Characters](https://lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/)|[Python](two_sum_two_pointers/longest_substr_with_longest_k_distinct_chars.py)||
|388|[Permutation Sequence](https://lintcode.com/problem/permutation-sequence/)|[Python](dfs_perm_comb/permutation.py)||
|389|[Valid Sudoku](https://lintcode.com/problem/valid-sudoku/)|[Python](dfs_perm_comb/valid_soduku.py)||
|392|[House Robber](https://lintcode.com/problem/house-robber/)|[Python](dp/house_robber.py)||
|393|[Best Time to Buy and Sell Stock IV](https://lintcode.com/problem/best-time-to-buy-and-sell-stock-iv/)|[Python](dp/stock.py)||
|397|[Longest Continuous Increasing Subsequence](https://lintcode.com/problem/longest-continuous-increasing-subsequence/)|[Python](easy/longest_continuous_increase_subsequence.py)||
|406|[Minimum Size Subarray Sum](https://lintcode.com/problem/minimum-size-subarray-sum/)|[Python](two_sum_two_pointers/minimun_size_subarray_sum.py)|sliding_window|
|407|[Plus One](https://lintcode.com/problem/plus-one/)|[Python](easy/plus_one.py)||
|408|[Add Binary](https://lintcode.com/problem/add-binary/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/add_bigint_string.cpp)||
|411|[Gray Code](https://lintcode.com/problem/gray-code/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/gray_code.rs), [Python](easy/gray_code.py)||
|415|[Valid Palindrome](https://lintcode.com/problem/valid-palindrome/)|[Python](palindrome/valid_palindrome.py)|two_pointers|
|418|[Integer to Roman](https://lintcode.com/problem/integer-to-roman/)|[Python](easy/int_to_roman.py)||
|419|[Roman to Integer](https://lintcode.com/problem/roman-to-integer/)|[Python](easy/int_to_roman.py)||
|423|[Valid Parentheses](https://lintcode.com/problem/valid-parentheses/)|[Python](collections/valid_parentheses.py)|stack|
|425|[Letter Combinations of a Phone Number](https://lintcode.com/problem/letter-combinations-of-a-phone-number/)|[Python](dfs_perm_comb/phone_9_keypad_combination.py)|product(笛卡尔积)|
|427|[Generate Parentheses](https://lintcode.com/problem/generate-parentheses/)|[Python](dfs_perm_comb/generate_parentheses.py)|回溯穷举|
|428|[Pow(x, n)](https://lintcode.com/problem/powx-n/)|[Python](math/pow.py)|binary_search, 快速幂运算|
|433|[Number of Islands](https://lintcode.com/problem/number-of-islands/)|[Python](graph/number_of_islands.py)|union_find, DFS, BFS|
|437|[Copy Books](https://lintcode.com/problem/copy-bookes/)|[Python](binary_search/copy_books.py)|dp, binary_search|
|440_LOCK|[Backpack III](https://lintcode.com/problem/backpack-iii/)|[Python](dp/backpack_3_item_can_select_multi.py)||
|442|[Implement Trie (Prefix Tree)](https://lintcode.com/problem/implement-trie-prefix-tree/)|[Python](tire/impl_tire_prefix_tree.py)|前缀树/字典树|
|443_LOCK|[Two Sum - Greater than target](https://lintcode.com/problem/two-sum-greater-than-target/)|[Python](two_sum_two_pointers/two_sum_le_count.py)|two_pointers|
|447_LOCK|[Search in a Big Sorted Array](https://lintcode.com/problem/search-in-a-big-sorted-array/)|[Python](binary_search/binary_search_unknown_size_sorted_array.py)|binary_search_first, 倍增法|
|451|[Swap Nodes in Pairs](https://lintcode.com/problem/swap-nodes-in-pairs/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/linked_list/swap_nodes_in_pairs.rs)||
|453|[Flatten Binary Tree to Linked List](https://lintcode.com/problem/flatten-binary-tree-to-linked-list/)|[Python](binary_tree/in_place_flatten_binary_tree_to_linked_list.py)||
|454|[Rectangle Area](https://lintcode.com/problem/rectangle-area/)|||
|457|[Classical Binary Search](https://lintcode.com/problem/classical-binary-search/)|[Python](binary_search/binary_search.py)|binary_search|
|458|[Last Position of Target](https://lintcode.com/problem/last-position-of-target/)|[Python](binary_search/binary_search_first_and_last.py)|binary_search|
|460|[Find K Closest Elements](https://lintcode.com/problem/find-k-closest-elements/)|[Python](binary_search/find_k_closest_elements.py)|binary_search|
|461|[Kth Smallest Numbers in Unsorted Array](https://lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/)|[Python](sorting_and_query/quick_select_kth_largest.py)||
|462|[Total Occurrence of Target](https://lintcode.com/problem/total-occurrence-of-target/)|[Python](binary_search/binary_search_first_and_last.py)||
|463|[Sort Integers](https://lintcode.com/problem/sort-integers/)|[Python](sorting_and_query/basic_sorting.py)|multi_solutions|
|464|[Sort Integers II](https://lintcode.com/problem/sort-integers-ii/)|[Python](sorting_and_query/basic_sorting.py)|multi_solutions|
|466|[Count Linked List Nodes](https://lintcode.com/problem/count-linked-list-nodes/)|||
|474_LOCK|[Lowest Common Ancestor II](https://lintcode.com/problem/lowest-common-ancestor-ii/)|[Python](binary_tree/binary_tree_lowest_common_ancestor.py)||
|476|[Stone Game(diff to leetcode)](https://lintcode.com/problem/stone-game/)|[Python](dp/stone_game_merge.py)||
|480|[Binary Tree Paths](https://lintcode.com/problem/binary-tree-paths/)|[Python](binary_tree/root_to_leaf_paths_find_all.py)|DFS, backtracking|
|484|[Swap Two Integers in Array](https://lintcode.com/problem/swap-two-integers-in-array/)|||
|486|[Merge K Sorted Arrays](https://lintcode.com/problem/merge-k-sorted-arrays/)|[Python](divide_conquer/merge_two_sorted_arrays.py)||
|488|[Happy Number](https://lintcode.com/problem/happy-number/)|[Python](easy/happy_number.py)||
|491|[Palindromic Number](https://lintcode.com/problem/palindrome-number/)|[Python](palindrome/longest_palindromic_substr.py)||
|492|[Implement Queue by Linked List](https://lintcode.com/problem/implement-queue-by-linked-list/)|[Python](collections/impl_queue_by_linked_list.py)||
|494|[Implement Stack by Two Queues](https://lintcode.com/problem/implement-stack-by-two-queues/)|[Python](collections/impl_stack_by_queue.py)||
|495|[Implement Stack](https://lintcode.com/problem/implement-stack/)|[Python](collections/impl_stack_by_queue.py)||
|512|[Decode Ways](https://lintcode.com/problem/decode-ways/)|[Python](dp/decode_ways.py)||
|513|[Perfect Squares](https://lintcode.com/problem/perfect-squares/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|517|[Ugly Number](https://lintcode.com/problem/ugly-number/)|[Python](easy/ugly_number.py)||
|521_LOCK|[Remove Duplicate Numbers in Array](https://lintcode.com/problem/remove-duplicate-numbers-in-array/)|[Python](partition_array/remove_duplicate_numbers_in_array.py)|partition_array|
|533_LOCK|[Two Sum - Closest to target](https://lintcode.com/problem/two-sum-closest-to-target/)|[Python](two_sum_two_pointers/two_sum_unique_pairs.py)|two_sum|
|534|[House Robber II](https://lintcode.com/problem/house-robber-ii/)|[Python](dp/house_robber.py)||
|535|[House Robber III](https://lintcode.com/problem/house-robber-iii/)|[Python](dp/house_robber.py)||
|539|[Move Zeros](https://lintcode.com/problem/move-zeroes/)|[Python](partition_array/move_zeros.py)|partition_array, 快慢双指针|
|544|[Top k Largest Numbers](https://lintcode.com/problem/top-k-largest-numbers/)|[Python](collections/top_k_largest_stream_min_heap.py)|min_heap|
|545|[Top k Largest Numbers II](https://lintcode.com/problem/top-k-largest-numbers-ii/)|[Python](collections/top_k_largest_stream_min_heap.py)|min_heap|
|547|[Intersection of Two Arrays](https://lintcode.com/problem/intersection-of-two-arrays/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|548|[Intersection of Two Arrays II](https://lintcode.com/problem/intersection-of-two-arrays-ii/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|562|[Backpack IV](https://lintcode.com/problem/backpack-iv/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|564|[Combination Sum IV](https://lintcode.com/problem/combination-sum-iv/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|563|[Backpack V](https://lintcode.com/problem/backpack-v/)|[Python](dp/backpack_5_plans_count.py)||
|577|[Merge k Sorted Interval Lists](https://lintcode.com/problem/merge-k-sorted-interval-lists/)|[Python](divide_conquer/merge_two_sorted_interval_lists.py)||
|578|[Lowest Common Ancestor III](https://lintcode.com/problem/lowest-common-ancestor-iii/)|[Python](binary_tree/binary_tree_lowest_common_ancestor.py)||
|582|[Word Break II](https://lintcode.com/problem/word-break-ii/)|[Python](dp/word_break_2.py)||
|584|[Drop Eggs II](https://lintcode.com/problem/drop-eggs-ii/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/dp/drop_eggs.rs)|dp|
|585_LOCK|[Maximum Number in Mountain Sequence](https://lintcode.com/problem/maximum-number-in-mountain-sequence/)|[Python](binary_search/mountain_array_max.py)|mountain_array, binary_search|
|586_LOCK|[Sqrt(x) II](https://lintcode.com/problem/sqrtx-ii/)|[Python](math/sqrt.py)|牛顿连续均值求根法|
|587_LOCK|[Two Sum - Unique pairs](https://lintcode.com/problem/two-sum-unique-pairs/)|[Python](two_sum_two_pointers/two_sum_unique_pairs.py)|two_sum|
|588|[Partition Equal Subset Sum](https://lintcode.com/problem/partition-equal-subset-sum/)|[Python](dp/backpack_1_2.py)|0-1背包问题|
|594|[Implement strStr() II](https://lintcode.com/problem/strstr-ii/)|[Python](string/find_substr.py)|kmp, Rabin-Karp(rolling_hash)|
|596_LOCK|[Minimum Subtree](https://lintcode.com/problem/maximum-subtree/)|[Python](binary_tree/subtree_max_sum.py)|divide_and_conquer|
|600|[Smallest Rectangle Enclosing Black Pixels](https://lintcode.com/problem/smallest-rectangle-enclosing-black-pixels)|[Python](binary_search/smallest_rectangle_enclosing_black_pixels.py)||
|603|[Largest Divisible Subset](https://lintcode.com/problem/largest-divisible-subset/)|[Python](dp/largest_divisible_subset.py)||
|604_LOCK|[Window Sum](https://lintcode.com/problem/window-sum/)|[Python](easy/window_sum.py)||
|606|[Kth Largest Element II](https://lintcode.com/problem/kth-largest-element-ii/)|[Python](sorting_and_query/quick_select_kth_largest.py)|quick_select, quick_sort, heap|
|607|[Two Sum III - Data structure design](https://lintcode.com/problem/two-sum-iii-data-structure-design/)|[Python](two_sum_two_pointers/two_sum_3_impl.py)|two_pointers|
|608|[Two Sum II - Input array is sorted](https://lintcode.com/problem/two-sum-ii-input-array-is-sorted/)|[Python](two_sum_two_pointers/two_sum_2_input_is_sorted.py)|two_pointers|
|609|[Two Sum - Less than or equal to target](https://lintcode.com/problem/two-sum-less-than-or-equal-to-target/)|[Python](two_sum_two_pointers/two_sum_le_count.py)|two_pointers|
|609|[Two Sum - Difference equals to target](https://lintcode.com/problem/two-sum-difference-equals-to-target/)|[Python](two_sum_two_pointers/two_sum_diff.py)|two_pointers|
|611_LOCK|[Knight Shortest Path](https://lintcode.com/problem/knight-shortest-path/)|[Python](bfs/knight_shortest_path.py)|bfs|
|612_LOCK|[K Closest Points](https://lintcode.com/problem/k-closest-points/)|[Python](sorting_and_query/k_closest_points_to_origin.py)|quick_select, sort_by_multi_keys|
|615|[Course Schedule](https://lintcode.com/problem/course-schedule/)|[Python](graph/course_schedule_2.py)|BFS, topological_sorting|
|616|[Course Schedule II](https://lintcode.com/problem/course-schedule-ii/)|[Python](graph/course_schedule_2.py)|BFS, topological_sorting|
|627|[Longest Palindromic Combination](https://lintcode.com/problem/longest-palindrome/)|[Python](palindrome/longest_palindromic_combination.py)|greedy|
|628|[Maximum Subtree](https://lintcode.com/problem/maximum-subtree/)|[Python](binary_tree/subtree_max_sum.py)|divide_and_conquer|
|630_LOCK|[Knight Shortest Path II](https://lintcode.com/problem/knight-shortest-path-ii/)|[Python](bfs/knight_shortest_path_2.py)|bfs|
|632|[Binary Tree Maximum Node](https://lintcode.com/problem/binary-tree-maximum-node/)|||
|633|[Find the Duplicate Number](https://lintcode.com/problem/find-the-duplicate-number/)|[Python](brain_twists/find_duplicate_number.py)|快慢双指针|
|654|[Sparse Matrix Multiplication](https://lintcode.com/problem/sparse-matrix-multiplication/)|[Python](math/sparse_matrix_multiplication.py)||
|655|[Add String](https://lintcode.com/problem/add-strings/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/add_bigint_string.cpp)||
|657|[Insert Delete GetRandom O(1)](https://lintcode.com/problem/insert-delete-getrandom-o1/)|[Python](collections/insert_delete_get_random_o1.py)||
|667|[Longest Palindromic Subsequence](https://lintcode.com/problem/longest-palindromic-subsequence/)|[Python](palindrome/longest_palindromic_subsequence.py)|dp(greedy)|
|668|[Ones and Zeroes](https://lintcode.com/problem/ones-and-zeroes/)|[Python](dp/backpack_ones_and_zeros.py)|完全背包问题|
|669|[Coin Change](https://lintcode.com/problem/coin-change/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|683|[Word Break III](https://lintcode.com/problem/word-break-iii/)|[Python](dp/word_break_3.py)||
|685|[First Unique Number in Data Stream](https://lintcode.com/problem/first-unique-number-in-data-stream/)|[Python](linked_list/first_unique_number_in_stream.py)||
|689|[First Unique Number in Data Stream](https://lintcode.com/problem/two-sum-iv-input-is-a-bst/)|[Python](binary_tree/bst_two_sum.py)||
|691|[Recover Binary Search Tree](https://lintcode.com/problem/recover-binary-search-tree/)|[Python](binary_tree/bst_recover_swap_two_nodes.py)||
|701|[Trim A Binary Search Tree](https://lintcode.com/problem/trim-a-binary-search-tree/)|[Python](binary_tree/bst_trim_in_range.py)||
|702|[Russian Doll Envelopes](https://lintcode.com/problem/russian-doll-envelopes/)|[Python](dp/russian_doll_envelopes.py)||
|719|[Calculate Maximum Value](https://lintcode.com/problem/calculate-maximum-value/)|[Python](dp/calculate_max_value_2.py)||
|724|[Minimum Partition](https://lintcode.com/problem/minimum-partition/)|[Python](dp/backpack_1_2.py)|0-1背包问题|
|740|[Coin Change 2](https://lintcode.com/problem/coin-change-2/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)|完全背包问题|
|741|[Calculate Maximum Value II](https://lintcode.com/problem/calculate-maximum-value-ii/)|[Python](dp/calculate_max_value_2.py)||
|749|[John's backyard garden](https://lintcode.com/problem/johns-backyard-garden/)|[Python](dp/backpack_4_coin_change_combination_sum_4.py)||
|761|[Smallest Subset](https://lintcode.com/problem/smallest-subset/)|[Python](easy/smallest_subset.py)||
|772|[Group Anagrams](https://lintcode.com/problem/group-anagrams/)|[Python](collections/group_anagrams.py)||
|773|[Vlid Anagram](https://lintcode.com/problem/vlid-anagram/)|[Python](collections/valid_anagram.py)||
|777|[Valid Perfect Square](https://lintcode.com/problem/valid-perfect-square/)|[Python](math/sqrt.py)||
|787|[The Maze](https://lintcode.com/problem/the-maze/)|[Python](bfs/the_maze.py)||
|793|[Intersection of Arrays](https://lintcode.com/problem/intersection-of-arrays/)|[Python](two_sum_two_pointers/intersection_of_two_arrays.py)||
|802|[Soduku Solver](https://lintcode.com/problem/soduku-solver/)|[Python](dfs_perm_comb/soduku_solver.py)||
|813|[Find Anagram Mappings](https://lintcode.com/problem/find-anagram-mappings/)|[Python](collections/mapping_two_anagram_list_int.py)||
|816|[Traveling Salesman Problem](https://lintcode.com/problem/traveling-salesman-problem/)|[Python](dfs_perm_comb/traveling_salesman_problem.py)||
|828|[Word Pattern](https://lintcode.com/problem/word-pattern/)|[Python](easy/word_pattern.py)||
|829|[Word Pattern II](https://lintcode.com/problem/word-pattern-ii/)|[Python](dfs_perm_comb/word_pattern_2.py)|DFS|
|835|[Number of 1Bits](https://lintcode.com/problem/hamming-distance/)|[Python](bitwise/number_of_1_bits.py)||
|839|[Merge Two Sorted Interval Lists](https://lintcode.com/problem/merge-two-sorted-interval-lists/)|[Python](divide_conquer/merge_two_sorted_interval_lists.py)||
|840|[Range Sum Query - Mutable](https://lintcode.com/problem/range-sum-query-mutable/)|[Python](segment_tree/segment_tree_range_sum.py)||
|841|[String Replace](https://lintcode.com/problem/string-replace/)|[Python](tire/string_replace.py)||
|845|[Greatest Common Divisor](https://lintcode.com/problem/greatest-common-divisor/)|[Python](math/greatest_common_divisor.py)||
|859|[Max Stack](https://lintcode.com/problem/max_stack/)|[Python](collections/max_stack.py)||
|871|[Minimum Factorization](https://lintcode.com/problem/minimum-factorization/)|[Python](factorization/minimum_factorization.py)|greedy|
|880|[Construct Binary Tree from String](https://lintcode.com/problem/construct-binary-tree-from-string/)|[Python](binary_tree/construct_from_string_with_parentheses.py)||
|887|[Super Egg Drop](https://lintcode.com/problem/super-egg-drop/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/dp/drop_eggs.rs)||
|891|[Valid Palindrome II](https://lintcode.com/problem/valid-palindrome-ii/)|[Python](palindrome/valid_palindrome_2.py)|two_pointers, greedy|
|892|[Alien Dictionary](https://lintcode.com/problem/alien-dictionary/)|[Python](graph/alien_dictionary.py)|heapq, topological_sorting|
|900|[Closest Binary Search Tree Value](https://lintcode.com/problem/closest-binary-search-tree-value/)|[Python](binary_tree/bst_closest_value.py)||
|901|[Closest Binary Search Tree Value II](https://lintcode.com/problem/closest-binary-search-tree-value-ii/)|[Python](binary_tree/bst_closest_value_2.py)||
|902|[Kth Smallest Element in a BST](https://lintcode.com/problem/kth-smallest-element-in-a-bst/)|[Python](binary_tree/traversal_pre_order.py)|DFS, stack|
|904|[Plus One Linked List](https://lintcode.com/problem/plus-one-linked-list/)|[Python](linked_list/bottom_up_plus_one_linked_list.py)||
|916|[Palindrome Permutation](https://lintcode.com/problem/palindrome-permutation/)|[Python](palindrome/palindrome_permutation.py)|greedy|
|943|[Range Sum Query - Immutable](https://lintcode.com/problem/range-sum-query-immutable/)|[Python](easy/range_sum_query_immutable.py)||
|954|[Insert Delete GetRandom O(1) - Duplicates allowed](https://lintcode.com/problem/insert-delete-getrandom-o1-duplicates-allowed/)|[Python](collections/insert_delete_get_random_o1.py)||
|955|[Implement Queue by Circular Array](https://lintcode.com/problem/implement-queue-by-circular-array/)|[Python](collections/impl_queue_by_circluar_array.py)||
|975|[2 Keys Keyboard](https://lintcode.com/problem/2-keys-keyboard/)|[Python](brain_twists/copy_paste_times.py)||
|976|[4Sum II](https://lintcode.com/problem/4sum-ii/)|[Python](two_sum_two_pointers/four_sum_2.py)|two_sum|
|980|[Basic Calculator II](https://lintcode.com/problem/basic-calculator-ii/)|[Python](brain_twists/calculator_2.py)||
|982|[Arithmetic Slices](https://lintcode.com/problem/arithmetic-slices/)|[Python](easy/arithmetic_slices.py)||
|995|[Best Time to Buy and Sell Stock with Cooldown](https://lintcode.com/problem/best-time-to-buy-and-sell-stock-with-cooldown/)|[Python](dp/stock.py)||
|1000|[Best Time to Buy and Sell Stock with Transaction Fee](https://lintcode.com/problem/best-time-to-buy-and-sell-stock-with-transaction-fee/)|[Python](dp/stock.py)||
|1010|[Max Increase to Keep City Skyline](https://lintcode.com/problem/max-increase-to-keep-city-skyline/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/max_increase_to_keep_city_skyline.rs)||
|1038|[Jewels and Stones](https://lintcode.com/problem/jewels-and-stones/)|[Python](easy/jewels_and_stones.py)||
|1057|[Network Delay Time](https://lintcode.com/problem/network-delay-time/)|[Python](bfs/network_delay_time_dijkstra.py)||
|1079|[Count Binary Substrings](https://lintcode.com/problem/count-binary-substrings/)|[Python](unclassified/count_binary_substring.py)||
|1115|[Average of Levels in Binary Tree](https://lintcode.com/problem/average-of-levels-in-binary-tree/)|[Python](binary_tree/traversal_level_order.py)||
|1137|[Construct String from Binary Tree](https://lintcode.com/problem/construct-string-from-binary-tree/)|[Python](binary_tree/construct_from_string_with_parentheses.py)||
|1153|[string sorting](https://www.lintcode.com/problem/string-sorting/)|||
|1162|[Merge Two Binary Trees](https://lintcode.com/problem/merge-two-binary-trees/)|[Python](binary_tree/merge_two_binary_tree.py)||
|1173|[Reverse Words in a String III](https://lintcode.com/problem/reverse-words-in-a-string-iii/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/easy/reverse_words_in_a_string_3.cpp)||
|1179_LOCK|[Friend Circles](https://lintcode.com/problem/friend-circles/)|[Python](graph/friend_circles.py)|union_find, DFS, BFS|
|1186|[Encode and Decode TinyURL](https://lintcode.com/problem/encode-and-decode-tinyurl/)|||
|1199|[Perfect Number](https://lintcode.com/problem/perfect-number/)|[Python](factorization/perfect_number.py)||
|1080|[Max Area of Island](https://lintcode.com/problem/max-area-of-island/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/bfs/max_area_of_island.rs)||
|1201|[Next Greater Element II](https://lintcode.com/problem/next-greater-element-ii/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/monotonic_stack/next_greater_element_2.rs)||
|1205|[Diagonal Traverse](https://lintcode.com/problem/diagonal-traverse/)|[Python](unclassified/diagonal_traverse.py)||
|1208|[Target Sum](https://lintcode.com/problem/target-sum/)|[Python](dp/backpack_1_target_sum.py)|0-1背包问题|
|1235|[Serialize and Deserialize BST](https://lintcode.com/problem/serialize-and-deserialize-bst/)|[Python](binary_tree/bst_serialize.py)|DFS, stack|
|1246|[Longest Repeating Character Replacement](https://lintcode.com/problem/longest-repeating-character-replacement/)|[Python](two_sum_two_pointers/longest_repeating_character_replacement.py)||
|1276|[Sum of Two Integers](https://lintcode.com/problem/sum-of-two-integers/)|[Python](bitwise/binary_addition.py)|binary_addition|
|1281|[Top K Frequent Elements](https://lintcode.com/problem/reverse-string/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/priority_queue/top_k_frequent_elements.rs)||
|1283|[Reverse Array](https://lintcode.com/problem/reverse-string/)|[Python](rotate_reverse_circle_shift/reverse_string.py)||
|1284|[Integer Break](https://lintcode.com/problem/integer-break/)|[Python](dp/integer_break.py)|划分类DP|
|1285|[Power of Four](https://lintcode.com/problem/power-of-four/)|[Python](bitwise/is_power_of_4.py)|bitwise|
|1294|[Power of Three](https://lintcode.com/problem/power-of-three/)|[Python](bitwise/is_power_of_3.py)|bitwise|
|1300|[Bash Game(Nim Game)](https://lintcode.com/problem/bash-game/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/nim_game.rs)||
|1311|[Lowest Common Ancestor of a Binary Search Tree](https://lintcode.com/problem/lowest-common-ancestor-of-a-binary-search-tree/)|[Python](binary_tree/bst_lowest_common_ancestor.py)||
|1319|[Contains Duplicate II](https://lintcode.com/problem/contains-duplicate-ii/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/contains_duplicate_2.rs)||
|1320|[Contains Duplicate](https://lintcode.com/problem/contains-duplicate-ii/)|||
|1332|[Number of 1 Bits](https://lintcode.com/problem/number-of-1-bits/)|[Python](bitwise/number_of_1_bits.py)||
|1333|[Reverse Bits](https://lintcode.com/problem/reverse-bits/)|[Python](bitwise/number_of_1_bits.py)||
|1334|[Rotate Array](https://lintcode.com/problem/rotate-array/)|[Python](rotate_reverse_circle_shift/rotate_array_right_circle_shift_elements.py)|reverse, circle_shift|
|1343|[Sum of Two Strings](https://lintcode.com/problem/sum-of-two-strings/)|[Python](easy/sum_of_to_strings.py)||
|1354|[Pascals Triangle II](https://lintcode.com/problem/pascals-triangle-ii/)|[Python](easy/pascals_triangle.py)||
|1355|[Pascals Triangle](https://lintcode.com/problem/pascals-triangle/)|[Python](easy/pascals_triangle.py)||
|1363|[ZigZag Conversion](https://lintcode.com/problem/zigzag-conversion/)|[Python](string/zigzag_conversion.py)||
|1375|[Substring With At Least K Distinct Characters](https://lintcode.com/problem/substring-with-at-least-k-distinct-characters/)|[Python](two_sum_two_pointers/substring_with_at_least_k_distinct_characters.py)||
|1424|[Longest Mountain in Array](https://lintcode.com/problem/longest-mountain-in-array/)|[Python](binary_search/mountain_array_longest.py)|mountain_array|
|1428|[Keys and Rooms](https://lintcode.com/problem/keys-and-rooms/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/keys_and_rooms.cpp)||
|1479|[Can Reach The Endpoint](https://lintcode.com/problem/can-reach-the-endpoint/)|[Python](bfs/can_reach_the_end_point.py)|bfs|
|1492|[Koko Eating Bananas](https://lintcode.com/problem/koko-eating-bananas/)|[Python](binary_search/koko_eating_bananas.py)||
|1499|[Reordered Power of 2](https://lintcode.com/problem/reordered-power-of-2/)|[Python](brain_twists/reordered_power_of_2.py)|permutation|
|1508|[Score After Flipping Matrix](https://lintcode.com/problem/score-after-flipping-matrix/)|[Python](greedy/score_after_flipping_matrix.py)|greedy|
|1524|[Search in a Binary Search Tree](https://lintcode.com/problem/search-in-a-binary-search-tree/)|[Python](binary_tree/bst_search.py)||
|1525|[N-ary Tree Postorder Traversal](https://lintcode.com/problem/n-ary-tree-postorder-traversal/)|[Python](easy/n_ary_tree_preorder_postorder.py)||
|1529|[N-ary Tree Preorder Traversal](https://lintcode.com/problem/n-ary-tree-preorder-traversal/)|[Python](easy/n_ary_tree_preorder_postorder.py)||
|1533|[N-ary Tree Level Order Traversal](https://lintcode.com/problem/n-ary-tree-level-order-traversal/)|[C++](https://github.com/pymongo/cpp_learn/blob/master/leetcode/bfs/n_ary_tree_level_order.cpp)||
|1535|[To Lower Case](https://lintcode.com/problem/to-lower-case/)|[Rust](https://github.com/pymongo/rust_leetcode/blob/master/src/easy/to_lowercase.rs)||
|1536|[Find First and Last Position of Element in Sorted Array](https://lintcode.com/problem/find-first-and-last-position-of-element-in-sorted-array/)|[Python](binary_search/binary_search_first_and_last.py)|binary_search|
|1593|[Construct Binary Tree from Preorder and Postorder Traversal](https://lintcode.com/problem/construct-binary-tree-from-preorder-and-postorder-traversal/)|[Python](binary_tree/construct_from_pre_order_and_post_order.py)|DFS|
|1609|[Middle of the Linked List](https://lintcode.com/problem/middle-of-the-linked-list/)|[Python](linked_list/middle_of_linked_list.py)|list_node, 快慢指针|
|1777|[Circle Area](https://lintcode.com/problem/circle-area/)|||
|1790_LOCK|[Rotate String II](https://lintcode.com/problem/rotate-string-ii/)|[Python](rotate_reverse_circle_shift/rotate_string_2.py)|reverse, circle_shift|
|1848_ABANDONED|[Word Search III](https://lintcode.com/problem/word-search-iii/)|[Python](dfs_perm_comb/word_search_3.py)||
|1870|[number of substrings with all zeroes](https://lintcode.com/problem/number-of-substrings-with-all-zeroes/)|[Python](two_sum_two_pointers/number_of_substrings_with_all_zeroes.py)||
|1872|[Longest Common Subsequence](https://lintcode.com/problem/minimum-cost-to-connect-sticks/)|[Python](easy/minimum_cost_to_connect_sticks.py)||
|1876|[Alien Dictionary(easy)](https://lintcode.com/problem/alien-dictionaryeasy/)|[Python](unclassified/verifying_an_alien_dictionary.py)||
|1901|[Squares of a Sorted Array](https://lintcode.com/problem/squares-of-a-sorted-array/)|||


---

# Category

## Dynamic Programming

### 划分型动态规划

戳气球(dp/burst_ballon.py)、石子归并(dp/stone_game_merge.py)

### 选或不选类DP

#### 打家劫舍系列

#### 股票买卖系列

### TODO 计数型动态规划

TODO k sum

## Palindrome

### Palindrome Sequence

- [Longest Palindromic Subsequence](https://lintcode.com/problem/longest-palindromic-subsequence) | [Python](palindrome/longest_palindromic_subsequence.py) | dp(greedy)
- [Valid Palindrome II](https://lintcode.com/problem/valid-palindrome-ii/) | [Python](palindrome/valid_palindrome_2.py) | two_pointers, greedy

### Palindrome Permutation

- [Longest Palindromic Combination](https://lintcode.com/problem/longest-palindrome) | [Python](palindrome/longest_palindromic_combination.py) | greedy
- [Palindrome Permutation](https://lintcode.com/problem/palindrome-permutation/) | [Python](palindrome/palindrome_permutation.py) | greedy

## greedy

- [Gas Station](https://lintcode.com/problem/gas-station/) | [Python](greedy/gas_station.py) | greedy
- [Maximum Subarray](https://lintcode.com/problem/maximum-subarray/) | [Python](greedy/maximum_subarray.py) |greedy, dp

---

主要用Python、Rust、C++、Go、Java这几种编程语言刷题

Rust性能与C++相当，大部分题都能和C++一样跑进0ms。

而且Rust有类似npm但比npm更好用更工程化的cargo工具，cargo运行单元测试/性能测试很简单，无论rs文件在哪，只要方法名上加#\[test]就能运行

我习惯通过单步调试+纸笔推演去读懂别人的优秀算法，但是Rust的单步调试经常跳到汇编代码中，按半天F7/F8才能跳出来，所以需要先用Go语言去理解我不懂的算法。

Java的优点不用我多说，借助maven+junit让我轻松地通过TDD的方式刷题，因为Java的语法类似C++，所有用Java也算了解用C++刷leetcode的心愿。

使用Java的另一个原因是，在某些题(如two sum)上Java(1ms)的性能比Go(4ms)还好。

而且Python的单元测试也简单，还支持typehint，更重要的是国内的面试官大部分都懂python代码

## pip和pipenv

python自带的pip没有类似`pom.xml`或`package.json`之类管理项目第三方依赖的清单文件

> pipenv uses Pipfile and Pipfile.lock

所以推荐用pyenv管理python版本，pipenv管理第三方依赖

## Python测试用例可读性

```python
import unittest
from copy import deepcopy

def solution(nums, target): pass

class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
    ]

    def test(self):
        for nums, target, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, solution(nums, target))
```

另一种提高单元测试-测试用例可读性的方法，用namedtuple，例如Point = namedtuple('Point', ['x', 'y']) 会生成/定义一个含有x,y字段的Point类