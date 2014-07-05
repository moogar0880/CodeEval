#!/usr/bin/perl
use feature qw(say);
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");

my $name_map = {zero => 0, one => 1, two => 2, three => 3, four => 4, five => 5,
                six => 6, seven => 7, eight => 8, nine => 9};
my $output;
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/);
    $line =~ s/(^s|s*$)//g;
    $output = '';
    @nums = split(';', $line);

    for $num (@nums){
        $output .= $name_map->{$num};
    }
    say($output);
}
close(INFILE);