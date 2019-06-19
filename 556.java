 public int nextGreaterElement(int n) {
        if(n<10){
            return -1;
        }    
        StringBuilder val = new StringBuilder(Integer.toString(n));
        Stack<Integer> stk = new Stack();
        for(int i=val.length()-1; i>0; i--) {
            while(i>0 && val.charAt(i-1) >= val.charAt(i)) { //Step 1
                stk.add(i);
                i--; 
            }
            if(i>0) { //Step 3
                char noToReplace = val.charAt(i-1);
                int nextGreaterIdx =  i; 
                while(!stk.isEmpty() && val.charAt(stk.peek())>noToReplace) { //Step 4
                    nextGreaterIdx = stk.pop();
                }
                
                val.setCharAt(i-1, val.charAt(nextGreaterIdx)); //Step 5
                val.setCharAt(nextGreaterIdx, noToReplace);
                char[] tempA = val.substring(i).toCharArray();
                Arrays.sort(tempA);//Step 6
                String newStr = val.substring(0, i) + new String(tempA);
                return new Long(newStr) > Integer.MAX_VALUE ? -1 : new Integer(newStr);
            }
        }
        return -1;         
    }