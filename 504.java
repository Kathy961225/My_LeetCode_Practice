class Solution {
    public String convertToBase7(int num) {
        if(num == 0) {
            return "0";
        }
        StringBuilder result = new StringBuilder();
        boolean is_negative = false;
        if(num < 0) {
            num *= -1;
            is_negative = true;
        }

        while(num > 0) {
            int temp = num % 7;
            num /= 7;
            result.insert(0, temp);
        }
        if(is_negative){
            result.insert(0, "-");
        }
        return result.toString();
    }
    
}