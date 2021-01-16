#include <iostream>
#include <vector>
#include <numeric>
#include <set>

using std::set;
using std::vector;

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        std::set<int> unique_nums;
        auto total = std::accumulate(nums.begin(), nums.end(), 0L);
        for (auto &&x : nums)
            unique_nums.emplace(x);
        auto unique_total = std::accumulate(unique_nums.begin(), unique_nums.end(), 0L);
        return (3 * unique_total - total) / 2;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {7, 3, 7, 7};
    std::cout << s.singleNumber(nums);
}