// PROBLEM TO SOLVE : 
// SINGLE NUMBER LEETCODE : 
#include <iostream> 
using namespace std; 

class Solution{
    public: 
        int singleNumber(vector<int> &nums){ 
             int ans = 0 ; 
             for(int val:nums){ 
                  ans = ans ^ val ;      //?    (^) XOR 
             }

        return ans;
        }
};




int main(){ 
      vector <int> nums = {4 ,1,2,2,1};
      Solution s;   // Object Creation in C++ 
      int value = s.singleNumber(nums);
      cout << value << endl; 
}