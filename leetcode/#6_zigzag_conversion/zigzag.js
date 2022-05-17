/**
 * @param {string} s the input string
 * @param {number} numRows the number of rows to zigzag up on down with
 * @return {string} the zigzagged string
 */
 var convert = function(s, numRows) {
    
    let result = "";
    
    // the distance between indices of each character from one "column" away in the same row
    let columnDist = 1 + Math.max(0, 2 * (numRows-1) - 1);
        
    for(let row = 0; row < numRows; row++){
        
        // start at the next row of the first column
        let index = row;
        
        while(index < s.length){
            result += s.charAt(index);
            
            // decide if we need to add another character on the diagonal, and avoid out of bounds error
            let nextCharDist = 2 * (numRows - row - 1);
            if((nextCharDist != 0) && (nextCharDist != columnDist) && (index + nextCharDist < s.length)){
                result += s.charAt(index + nextCharDist);
            }
                
            index += columnDist;
        }
    }
    
    return result;
};