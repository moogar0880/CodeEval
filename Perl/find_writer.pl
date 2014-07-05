#!/usr/bin/perl
use feature qw(say);
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");

my $output;
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/);
    $line =~ s/(^s|s*$)//g;
    $output = '';
    @results = split('|', $line);
    say(@results[0]);
    $letters = $results[0];
    $indicies = $results[1];
    # say($letters);
    # say($indicies);
    for my $index ($indicies){
        $output .= $letters[$index - 1];
    }
    # say($output);
}
close(INFILE);