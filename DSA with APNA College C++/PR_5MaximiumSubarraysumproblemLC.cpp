//! Maximum SubArray Sum 
#include <iostream> 
using namespace std ;

int max_sum = INT_MIN ;

// int MaximumSubArraySum(int arr[] , int n ){ 
//     //? Maximum SubArray's Sum : 

//    for (int st=0 ; st<n ; st++){ 
//        int curr_sum = 0 ; 
//        for (int end=st ; end<n-1 ; end++){ 
//              curr_sum += arr[end];
//              max_sum =max(curr_sum ,max_sum);
//        }
//    }
//    return max_sum ;  //TC ==> O(N^2)

// };

//! KADANE'S ALGORIGM FOR MAXIMUM SUBARRAY (MOST OPTIMISED)
int KadaneAlgo(int arr[] , int n){ 
    
    int curr_sum =0 ;
    for (int i=0 ; i<n ; i++){ 
           curr_sum += arr[i];
           max_sum = max(curr_sum , max_sum);
           if (curr_sum < 0){ 
                curr_sum = 0 ; 
           }
    }
  return max_sum ;
};




int main(){ 
   int n=5 ; 
   int arr[5] = {1,2,3,4,5};

  //  //? ALL POSSIBLE SUBARRAYS : 
  //  for (int st=0 ; st<n ; st++){ 
  //     for (int end=st ;end<n-1 ;end++ ){ 
  //         for(int i=st ; i<=end ; i++){ 
  //               cout << arr[i];
  //         }
  //         cout << " " ; 
  //     }
  //     cout << endl; 
  //  }
 
  //  cout << MaximumSubArraySum(arr,n) << endl; 

   cout << KadaneAlgo(arr , n) << endl ; 





  return 0 ; 
}