#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:

    int maxTurbulenceSize(vector<int>& A) {
        size_t sz = A.size();
        if(sz < 2) return sz;

        
        int sub_arr_sz = 1;
        int prev = A[1] - A[0];
        int result = prev != 0 ? 2 : 1;
        for(int i=1; i < sz-1; ++i)
        {
            int curr = A[i+1] - A[i];
            if((prev > 0 && curr < 0) ||
               (prev < 0 && curr > 0) ||
               (prev != 0 && curr == 0))
            {
                ++sub_arr_sz;
            }
            else
            {
                sub_arr_sz = 1;
            }
            
            result = max(result, sub_arr_sz);
            prev = curr;
        }
        return result;
    }
};

int main(int argc, char* argv[])
{
    Solution s;

    vector<int> input1 {9,4,2,10,7,8,8,1,9};
    vector<int> input2 {4,8,12,16};
    vector<int> input3 {100};
    vector<int> input4 {9,9};
    vector<int> input5 {2,0,2,4,2,5,0,1,2,3};

    cout << s.maxTurbulenceSize(input1) << "\n";
    cout << s.maxTurbulenceSize(input2) << "\n";
    cout << s.maxTurbulenceSize(input3) << "\n";
    cout << s.maxTurbulenceSize(input4) << "\n";
    cout << s.maxTurbulenceSize(input5) << "\n";

    return 0;
}