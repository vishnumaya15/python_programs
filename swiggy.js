//function to find non repeating letter and count of it
// const word = "sqioojsajka";
const word = [ 1, 2,3,4,4];

function getLetterOccurrences(word) {
    const letterCount = {};
    const repeatingLetter = {};

    for (const i of word) {        
        letterCount[i] = (letterCount[i] || 0) + 1;
        console.log("letter",i,letterCount[i]);
        

        for(let j in letterCount){
            if(letterCount[j]>1){
                repeatingLetter[j] = letterCount[j];

            }
        }
    } 

        return repeatingLetter;
    }

const result = getLetterOccurrences(word);

console.log(result);

//function to find just the non repeating letters
function findRepeatingLetters(word) {
    const frequency = {};
    const repeatingLetters = new Set();

    for (let letter of word) {
        letter = letter.toUpperCase();
        if (frequency[letter]) {
            frequency[letter]++;
            repeatingLetters.add(letter);
        } else {
            frequency[letter] = 1;
        }
    }

    return [...repeatingLetters];
}
const word1 = "SWiiugvhgvghbbnmIGGY";
const repeating = findRepeatingLetters(word1);

if (repeating.length > 0) {
    console.log("Repeating letter(s):", repeating.join(", "));
} else {
    console.log("No repeating letters.");
}


// function to find only the first repeating letter
function firstNonRepeatingChar(str) {
    const letterCount = {};

    // Count occurrences of each character
    for (const letter of str) {
        // console.log("occur",letter);
        letterCount[letter] = (letterCount[letter] || 0) + 1;;
         
    }
    // Find the first character with count 1
    for (const letter of str) {
        // console.log("letter",letter);
        
        if (letterCount[letter] === 1) {
            return letter;
        }
    }

    return null;
}

// Test cases
console.log(firstNonRepeatingChar("swiss")); // Output: "w"
console.log(firstNonRepeatingChar("aabbcc")); // Output: null
console.log(firstNonRepeatingChar("apple")); // Output: "a"
console.log(firstNonRepeatingChar("racecar")); // Output: "e"

//first duplicate of an array or string
function findFirstDuplicate(input) {
    const seen = new Set();

    for (let element of input) {
        if (seen.has(element)) {
            return element;
        }
        seen.add(element);
    }

    return null; // No duplicates found
}

// Examples with string
console.log(findFirstDuplicate("swiiggy"));  // Output: "g"
// Examples with array
console.log(findFirstDuplicate([1, 2, 3, 4, 2, 5]));  // Output: 2
console.log(findFirstDuplicate(['a', 'b', 'c', 'a']));  // Output: "a"


function firstNonRepeat(str) {
    for (let char of str) {
      if (str.indexOf(char) === str.lastIndexOf(char)) {
        return char;
      }
    }
    return null;
  }
console.log("NON",firstNonRepeat("aabbvvnmkslcnsnnn"));

function encryptString(str) {
  let result = '';
  let count = 1;

  for (let i = 1; i <= str.length; i++) {
    if (str[i] === str[i - 1]) {
      count++;
    } else {
      result += str[i - 1] + (count > 1 ? count : '');
      count = 1;
    }
  }

  return result;
}

// Example
console.log(encryptString("saaavvvvvqql")); // 
  
function countUniqueElements(arr) {
  const unique = new Set(arr);
  return unique.size;
}

// Example
console.log(countUniqueElements([1, 2, 2, 3, 4, 4, 5])); // Output: 5



function twoSum(nums, target) {
    const map = new Map();  // To store numbers and their indices.
    for (let i = 0; i < nums.length; i++) {
        
        const complement = target - nums[i];
        console.log("COMPL",complement);
        

        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return []; // In case no solution is found (optional, given the problem guarantees one solution).
}

// Example Usage:
console.log(twoSum([2, 7, 11, 15], 9)); // Output: [0, 1]



