prompt = '> '
puts "Enter number of people:"
print prompt

people = gets.chomp.to_i

puts "How many trials should I do?"
print prompt

trials = gets.chomp.to_i

count = 0

for i in (0...trials)
  birthdays = []
  #make random birthdays.
  for j in (0...people)
    birthdays.push(rand(365)) 
  end

  #check for repeats
  if not ( birthdays.length == birthdays.uniq.length )
    count = count + 1
  end
end

same_ratio = count.to_f / trials * 100

puts "Same probability = #{same_ratio}%"

puts
