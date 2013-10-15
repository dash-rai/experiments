=begin

For question, see https://code.google.com/codejam/contest/351101/dashboard#s=p0

This question was asked as part of Google code jam's qualification round for Africa, 2010.

Successfully solves both large and small inputs.

To execute, run "ruby store_credit.rb > output_file"

=end

input_file_name = "input" #Input file.

#open file
f = File.open(input_file_name) or abort "Unable to open file..."

inputArray = []

f.each_line do |line|
  inputArray.push line
end

N = inputArray[0].to_i

(0...N).each do |i|
  credit = inputArray[i*3 + 1].to_i
  items = inputArray[i*3 + 2].to_i
  item_list = inputArray[i*3 + 3].split(' ').map {|x| x.to_i}
  catch :done do
    (0...(items-1)).each do |j|
      (j+1...items).each do |k|
        if item_list[j] + item_list[k] == credit
          puts "Case \##{i+1}: #{j+1} #{k+1}"
          throw :done
        end
      end
    end
  end
end
