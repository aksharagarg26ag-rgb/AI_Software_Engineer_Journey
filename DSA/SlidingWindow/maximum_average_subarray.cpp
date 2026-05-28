// Problem: Maximum Average Subarray I
// Topic: Sliding Window
// Time Complexity: O(n)

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {

        int sum = 0;

        // first window
        for(int i = 0; i < k; i++){
            sum += nums[i];
        }

        int maxSum = sum;

        // slide window
        for(int i = k; i < nums.size(); i++){

            sum = sum - nums[i-k] + nums[i];

            maxSum = max(maxSum, sum);
        }

        return (double)maxSum / k;
    }
};