//!  PASS BY REFERENCE : 

// #include <iostream> 
// using namespace std; 


// void callbyreference(int arr[3]){ 
//   cout << "IN FXN " << endl ; 
//    for(int i=0 ; i<3 ; i++){ 
//        arr[i] = arr[i]*2;
//    }
// }
// int main(){ 
//   int arr[3] = {1,2,3}; 
//   callbyreference(arr);
//   cout << "IN MAIN " << endl ; 
//   for (int i=0 ; i<3 ; i++){ 
//      cout<< arr[i] << " ";
//   }
//    return 0 ; 
// }
// -----------------------------------------------------------------------------


// //! LINEAR SEARCH : 
// #include <iostream> 
// using namespace std ; 

// int LinearSearch(int nums[],int target){
//    for (int i=0 ; i<8 ; i++){ 
//        if (nums[i] == target){   //FOUND 
//            return i ; 
//        }
//    }
//    return -1 ;  //not found 
// }

// int main(){ 
//    int arr[8] = {1,4,2,5,7,6,9,2};
//    int target = 9 ; 
//    cout << "The index the Target was : " << LinearSearch(arr , target) << endl;


// }

// -----------------------------------------------------------------------------

// ! REVERSE AN ARRAY : 

// #include <iostream> 
// using namespace std ; 

// void  reverse_array (int nums[] ,int sz){ 
//   int j = sz-1 ;
//    for (int i=0 ; i<sz/2 ; i++){ 
//       int temp = nums[i];
//       nums[i] = nums[j];
//       nums[j] =temp ; 
//       j -= 1 ; 
//       if (nums[i] == nums[j]){ 
//          break ; 
//       }
//   }
// }


// REVERSE FOR LOOP LOGIC : 
// void reverse_array2(int nums[] , int sz){ 
//    for(int i=sz-1 ; i>=0 ; i--){ 
//       cout<< nums[i] << endl; 
//    }
// }
// int main(){ 
//   int sz = 5;
//   int nums[] = {1,2,3,4,5};

//  reverse_array2(nums,sz);
 // For priniting : 
//  for (int i =0 ; i < sz ; i++ ){ 
//    cout << nums[i] << endl; 
//  }
//  }


// -----------------------------------------------------------------------------
// PRACTICE QUESTIONS TO SOLVE : 

// ! 1 : SUM AND PRODUCT OF ALL NUMBERS IN AN ARRAY 
// #include <iostream> 
// using namespace std ; 


// int sum_product (int arr[] , int sz){
//   int sum = 0 ; 
//   int product = 1 ; 
//    for (int i=0 ; i<sz ; i++){ 
//          sum += arr[i] ; 
//          product *= arr[i] ; 
//    }
//   cout << "Sum of all Numbers is : "<<  sum  << endl; 
//   return  product ;
// }
// int main(){ 
//   int sz = 5 ; 
//   int arr[] = {1,2,3,4,5}; 
//   cout << sum_product(arr,sz);
 

// }


// -----------------------------------------------------------------------------

// SWAP MIN AND MAX NUMBERS IN ARRAY : O(N)

// #include <iostream> 
// using namespace std ; 
// void find(int arr[] ,int sz ){ 
//     int smallest = arr[0] ;
//     int largest  = arr[0];
//     for(int i=0 ; i<sz ; i++){ 
//         smallest = min(smallest , arr[i]);
//         largest = max(largest , arr[i]);
//     }
//   int value=1 ; 
//   int value2=1 ;
//    for (int i=0 ; i<sz ; i++){ 
//         if (smallest == arr[i]){ 
//             value  = i ; 
//         }
//         if (largest == arr[i]){ 
//              value2 = i ; 
//         }
//    }
//         int temp = arr[value];
//         arr[value] = arr[value2]; 
//         arr[value2] =temp ; 
//         cout << arr[value] << endl ;
//         cout << arr[value2] << endl;

//   }



// int main(){ 
//     int sz =5 ; 
//     int arr[] = {1,2,3,4,5}; 

//    find(arr,sz);
//    for(int i=0 ;i<sz ;i++){ 
//       cout<< arr[i] << " " ; 
//    }
// }


// -----------------------------------------------------------------------------

//! UNIQUE VALUES IN AN ARRAY : 

#include <iostream> 
using namespace std ; 

int main(){ 
   int sz = 6 ; 
   int arr[] = {1,1,2,3,2,4,5};
   std::vector<int> arr2;
   for (int i=1 ; i<sz ; i++){ 
      if (arr[i] != arr[i-1]){ 
          arr2.push_back(arr[i]) ;
      }
      else { 
         continue ; 
      }
   }
   for (int i=0 ; i<sizeof(arr2)/sizeof(int) ; i++){
       cout << arr2[i] ; 
   }

}





// -----------------------------------------------------------------------------

















// -----------------------------------------------------------------------------











