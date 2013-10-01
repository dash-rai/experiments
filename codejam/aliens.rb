=begin
     input_file_name = 'input'

     f = File.open(input_file_name) or abort "Unable to open file #{input_file_name}."

     input_array = []

     f.each_line do |line|
      input_array.push line
    end

     L = input_array[0].split(' ').[0].to_i
     D = input_array[0].split(' ').[1].to_i
     N = input_array[0].split(' ').[2].to_i
=end

#put whole string to array into a function and return resulting array
word = "(zxy)bc"


#repeat for every line

##### DUDE, what about regular expressions? See if z or x or y and b and c match the pattern given. That's still requiring the following code though. We'll figure something out. Keep calm and code on.

def word_array(word)
  word = word.split('')
  word_array = []
  
  loop do
    char = word.shift #Pops the first element of the array
    break if char == nil
    if char == '('
      poss_array = []
      loop do #Infinite loop until broken
        char = word.shift
        break if char == ')'
        poss_array.push(char)
      end
      word_array.push(poss_array)
      
    else
      word_array.push(char)
    end

  end
  return word_array
end

def num_of_poss (word_array)
  count = 1
  for elem in word_array
    if elem.is_a? Array
      count *= elem.length
    end
  end
  return count
end

arr = word_array(word)
n = num_of_poss(arr)

all = []

for elem in arr
  if elem.is_a? Array

  else
    all

# is_a? Array
# permutation.to_a

