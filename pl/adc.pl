#!/usr/bin/perl
##########################################################################################
#                                                                                        #
#                                ADSERVER  LOG   ANALYSIS                                #
##########################################################################################

#==================================================================================MODULES

#use strict;
use Getopt::Std;
use Time::Local;

#=========================================================================================

#---------------------------------------------------------------------------INITIALISATION
    my $noneedtime=0;
    my $errors=0;                          #default value is 0
    my $timeouts=1;                        #default value is 0
    my $end_time_minutes=5;                #default value is 5 minutes
    my $end_time_hours=0;                  #default value is 0 hours
    my $data_of_stat='';

    my %host_hash=();
    my $proc_file="/home/y/conf/ads/adsystem.procinfo";
    my @stat_file_name= </home/y/logs/ads/*.stats>;
    my $stat_file=$stat_file_name[0];
    my $err_file=</home/y/logs/ads/adsvrshm_*.err>;
    my %month_hash=("Jan",0,"Feb",1,"Mar",2,"Apr",3,"May",4,"Jun",5,"Jul",6,"Aug",7,"Sep",8,"Oct",9,"Nov",10,"Dec",11);
    my $time_of_stat=0;
    my $var=0;
    my  %err_hash=();
    my ($host ,$time ,$spaceid)='';
    my $cmd_date='';
#------------------------------------------------------------COMMAND LINE OPTION VARIABLES

    my $start_year;
    my $start_month;
    my $start_minutes=0;
    my $start_sec=0;
    my $start_day=0;
    my $start_hours=0;
    my $start_time=0;
    my $end_sec=0;

#-------------------------------------------------------------COMMAND LINE VALUES ASSIGING
     $SC_USAGE="USAGE:[-s] [-c]\n
     [-s] AdServer\n
     [-c] AdClient\nTry Again!!\n";
    my %options =();
    getopts("scd:e:t:i:",\%options);

    die "Choose either [-s] or [-c]!!\n" if(defined($options{c}) and defined($options{s}));
    die "Choose either [-s] or [-c]!!\n" if(!defined($options{c}) and !defined($options{s}));

#---------------------------------------------------------------------------------AD CLIENT
    if(defined $options{c})
    {
            my $start_flag=0;
            my $line_of_proc='';
            my $host_from_proc='';
            my $host_from_stat='';
            my $start_hhmmss='';
            my $interval=0;
            my $mid_time=0;

            $errors=$options{e} if(defined $options{e});

               $timeouts= $options{t} if(defined $options{t});

            #$timeouts=$options{t} if(defined($options{t});
            $end_time_minutes=$options{m} if(defined $options{m});

            if(defined($options{d}))

                {
                   gettime();
                 }
            else
               {
                    $end_sec=todaytime();
                    $start_time=$end_sec-3*60*60;
               }

               print "The starting time is:$start_time\n";
               print "The end time is     :$end_sec\n";



               print "Start time should not be greater than or equal to end time" if($start_sec >= $end_sec);

               if(defined($options{i}))
               {
                       $interval=$options{i};
               }
               else
               {
                       $interval=10;
               }

             #OPEN THE PROCESS INFORMATION FILE

              open(PROC , "<$proc_file") or die("Cannot open the  $proc_file file!");

                 while($line_of_proc=<PROC>)
                       {

                               next if($line_of_proc!~/^shmproxy-ac_/);
                               chomp($2);
                               $host_hash{$2}='' if($line_of_proc=~/^shmproxy-ac_(\S+)\s+(\S+)/);

                       }

               close PROC;

            #CLOSING THE PROC  INFORMATION FILE


             # CREATING THE HASH FOR ERROR FILE
               open(ERR ,"<$err_file") or die("Cannot open the $err_file file!");

               while($line_of_err=<ERR>)
               {
                       next if( $line_of_err !~ m!(\S+)\s(.+)\:\sERROR:\ Invalid\ spaceid! );
                           if( $line_of_err =~ m!(\S+)\s(.+)\:\sERROR:\ Invalid\ spaceid\ (\S+)\ from\ (\S+),!){
                               ($ts ,$spaceid ,$host)=($2,$3,$4);
                              #print "the hostanem:$host\n";
                               if(defined($host_hash{$host}))
                                       {
                                           $time=`date -j -f "%b %d %T %Y" "$ts" "+%s"`;
                                               chomp($time);
                                               if($start_time <= $time and $time<= $end_sec)
                                               {
                                                       $err_hash{"$host"}{"$time"}{"spaceid"}=$spaceid;
                                               }

                                       }
                               }

               }

               close ERR;

               #OPENING THE  STATISTICS FILE

               open(STAT,"$stat_file") or die("Cannot open the $stat_file file!");

               while( $time_of_stat <= $end_sec and $data_of_stat=<STAT>)
                {

                    next if($data_of_stat=~/^key/);

                    #READING THE TIMINGS WITH IN THE FILE

                    if($data_of_stat=~/^ad server(.*)stats at\s(\S+)\s+(.+):/)
                      {
                           my $prev_time=$time_of_stat;
                           my $filetime=$3;
                           $time_of_stat=`date -j -f "%b %d %T %Y" "$filetime" "+%s"`;
                               if($start_flag==1)
                               {
                                       if($start_time<=$prev_time)
                                       {
                                               $start_time=$start_time+$interval*60;
                                       }
                               }

                       }

                   #GETTING THE HOST NAME FROM THE STAT FILE

                   if($data_of_stat=~/^host\s+(\S+):.*timeouts =\s([\d|\.]+),\s+errors = ([\d|\.]+).*avg lookup = ([\d|\.]+),\s+avg processing =\s([\d|\.]+)/)
                   {
                     $host_from_stat=$1;

                     #CHECKING THE EXISTANCE OF  HOST NAME IN PROC FILE

                     if($start_time <=$time_of_stat and exists($host_hash{$host_from_stat}))
                       {

                        my $invalid_spaceid='';
                       chomp($host_from_stat);
                        if(defined($err_hash{"$host_from_stat"}))
                               {
                                 #print $host_from_stat ,"\n";
                                       foreach $dat ( keys %{$err_hash{"$host_from_stat"}})
                                               {
                                                       if($dat >= $start_time and $dat <= $end_sec)
                                                       {
                                                               $x=$err_hash{"$host_from_stat"}{"$dat"}{spaceid};
                                                               chomp($x);
                                                               $invalid_spaceid=$invalid_spaceid.":$x";
                                                                              }
                                               }
                               }

                          if($2>=$timeouts and $3>=$errors)
                            {
                                    if($start_flag==0)
                                   {
                                           my  $x=localtime($start_time);
                                           my  $y=localtime($end_sec);
                                           printf("\n*************************************************************************************************************************");
                                           printf("\n*                              ADCLIENT   STATISTICS                                                                    *");
                                           printf("\n* Start Time::$x                   Thresholds of Timeouts=$timeouts,Errors=$errors                              *");
                                           printf("\n* End Time  ::$y                                                                                  *");
                                           printf("\n*************************************************************************************************************************");
                                           printf("\n+--------------------+----------------------------------------------+---------+-------+----------------+----------------+");
                                           printf("\n|Time Stamp          |HOST NAME                                     |Time Outs| Errors|  Avg Lookups   |Avg Processing  |");
                                           printf("\n+--------------------+----------------------------------------------+---------+-------+----------------+----------------+\n");
                                       $start_flag=1;
                                   }

                               #    my $display_time=`date -r $start_time '+%b %d %H:%M:%S'`;#i`date -r $time_of_stat '+%b %d %H:%M:%S'`;
                                #   chomp($display_time);
                                       chomp($time_of_stat);
                                        my $display_time=`date -r $time_of_stat "+%b %d %H:%M:%S"`;
                                               chomp($display_time);
                                  printf("\n|%18s  |",$display_time);
                                   printf("%-46s|",$host_from_stat);
                                   printf("%9d|",$2);
                                   printf("%7d|",$3);
                                   printf("%16.6f|",$4);
                                   printf("%16.6f|",$5);

                                 my    @invalid= split /:/ ,$invalid_spaceid;

                                          my %dup_hash = map { $_ ,1} @invalid ;
                                           @unique= keys %dup_hash;

                                      print @unique ,"\n";

                           }
                    }
                }
  #}
            }#end of the while

            if($start_flag==0)
            {
                               printf("\nNO DATA AVAILABLE !!\n") if($start_flag==0);
            }
             else
            {
                                       printf("\033[0m+--------------------+----------------------------------------------+---------+-------+----------------+----------------+\n");
             }
            close STAT;
     }


#--------------------------------------------------ADCLENT INFORMATION RETRIVAL OVER

       if(defined($options{s}))
       {
               my @individual=();my @total_values=();
               my $interval=10;   #default value is 10
               my $display_key=0;
               my $file_hhmmss=0;
               my $time='';

               $interval=$options{i} if(defined($options{i}));
               if(defined($options{d}))

                {
                   gettime();
                 }
               else
               {
                    $end_sec=todaytime();
                    $start_time=$end_sec-3*60*60;
               }

               print "The starting time is:$start_time\n";
               print "The end time is     :$end_sec\n";

               #OPENING OF THE STAT FILE

               open(STAT ,"< $stat_file");

               while( $time_of_stat <= $end_sec and $data_of_stat=<STAT>)
                {

                    next if($data_of_stat=~/^key/);

                    #READING THE TIMINGS WITH IN THE FILE

                    if($data_of_stat=~/^ad server(.*)stats at\s(\S+)\s+(.+):/)
                      {
                           $adserver=$1;
                           my $filetime=$3;
                           $time_of_stat=`date -j -f "%b %d %T %Y" "$filetime" "+%s"`;
                        }
                       if($time_of_stat >= $start_time)
                       {

                               @individual=($data_of_stat=~m/([\d|\.]+)\D+/g)  and  push(@total_values,@individual) if($data_of_stat=~/average lookup time|average processing time|number of no-spa
ce events|btlib/);

                               push(@total_values, $1 , $2 , $3)    if($data_of_stat=~/^uds2 min\/max\/avg\s+=\s+(\d+)\/(\d+)\/(\d+).*/);

                               if($data_of_stat=~/^uds2 successes =\s+(\d+),/)
                               {

                               if($start_flag==0)
                               {
                                       my $t=`date  -r $start_time `;
                                       chomp($t);
                                       printf("*******************************************************************************************************************************\n");
                                       printf("*                                         ADSERVER  HEALTH  CHECK  WITH  IN TIME INTERVALS                                    *\n");
                                       printf("*                                                                                                                             *\n");
                                       printf("*Ad Server ::$adserver\tStart time::$t\tTime Interval ::Every $interval Minutes\t\t\t   *\n");
                                       printf("*******************************************************************************************************************************\n");
                                       printf("+----------------+--------------+-------------+--------+--------------------------------+-------------------------------------+\n");
                                       printf("|Time            |    Avg       | Avg proce   |no space|            Btlib               |                Uds2                 |\n");
                                       printf("|Intervals       | Lookup time  | ssing time  |  events|inits   |fails|    max |  avg   | min    |    max |     avg|successes |\n");
                                       printf("+----------------+--------------+-------------+--------+--------+-----+--------+--------+--------+--------+--------+----------+");

                                       $start_flag=1;
                               }
                                       $time=localtime($start_time);
                                       printf("\n|%4s%3s%9s|",(( split /\s+/,$time)[1,2,3]));
                                       printf("%14.6f|",$total_values[0]);
                                       printf("%13.6f|",$total_values[1]);
                                       printf("%8d|",$total_values[2]);
                                       printf("%8d|",$total_values[3]);
                                       printf("%5d|",$total_values[4]);
                                       printf("%8d|",$total_values[5]);
                                       printf("%8d|",$total_values[6]);
                                       printf("%8d|",$total_values[7]);
                                       printf("%8d|",$total_values[8]);
                                       printf("%8d|",$total_values[9]);
                                       printf("%10d|",$1);
                                       @total_values=();
                                       $start_time=$start_time+$interval*60;
                                       $display_key=1;

                               }


                      }


               } # end of the while loop




 close STAT;

               if($start_flag==0)
               {
                               printf("\nNO DATA AVAILABLE !!\n");
               }
             else
               {
                               printf("\n+----------------+--------------+-------------+--------+--------+-----+--------+--------+--------+--------+--------+----------+\n");

               }


       }



  sub  gettime
   {
       $start_hours=0;
       $start_minutes=0;
       $start_sec=0;

       $start_year=`date "+%Y"`;

       $cmd_date=$options{d};
       chomp($cmd_date);

       if($cmd_date=~/(\S+)\s+(\d+)\s+(\d+)-(\d+)/)
       {

               $start_hours=$3;
               $end_minutes=$4-$3;$start_time=timelocal($start_sec, $start_minutes, $start_hours ,$2,$month_hash{$1},$start_year);
               $end_sec= $start_time + $end_minutes*60*60;
       }
       elsif($cmd_date=~/(\S+)\s+(\d+)\s+(\d+)\*/)
          {
               $start_hours=$3;
               $start_time=timelocal($start_sec, $start_minutes ,$start_hours, $2,$month_hash{$1} ,$start_year);
               $end_sec=todaytime();

               }
       elsif($cmd_date=~/(\S+)\s+(\d+)\s+(\d+)/)
      {
               $start_hours=$3;
               $start_time=timelocal($start_sec, $start_minutes, $start_hours ,$2,$month_hash{$1},$start_year);
                $end_sec=$start_time + 3600;
      }
       elsif($cmd_date=~/(\S+)\s+(\d+)/)
       {
               $start_time=timelocal($start_sec , $start_minutes , $start_hours ,$2 ,$month_hash{$1} ,$start_year);
               $end_sec=$start_time + 24*60*60;
       }
      else
      {
              print "Please enter the date as mentioned!\n";
      }

}

 sub todaytime
  {
     my $timestamp=`date "+%b %d %T %Y"`;
     chomp($timestamp);
     my $time=`date -j -f "%b %d %T %Y" "$timestamp" "+%s"`;
     return $time;
  }