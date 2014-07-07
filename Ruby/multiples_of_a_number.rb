File.open(ARGV[0]).each_line do |line|
  if line
    x, n = line.strip.split(',')
    x = x.to_i
    n = n.to_i
    val = n
    while val < x
      val += n
    end
    puts val
  end
end
