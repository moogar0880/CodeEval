File.open(ARGV[0]).each_line do |line|
  if line
    output = ''
    line.split(' ').each do |word|
      word[0] = word[0].upcase
      output << word + ' '
    end
    puts output[0..-1]
  end
end
