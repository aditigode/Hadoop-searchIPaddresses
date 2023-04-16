
#step 1
hadoop jar C:\Users\Aditi\OneDrive\Desktop\Courses\ECC\hadoop-3.2.1\hadoop-3.2.1\share\hadoop\tools\lib\hadoop-streaming-3.2.1.jar -input \Aditi\part1\access.log -output \Aditi\part1\output_part1_step1 -mapper "python C:\Users\Aditi\OneDrive\Desktop\Courses\ECC\hadoop-3.2.1\part1\mapper_chain1.py" -reducer "python C:\Users\Aditi\OneDrive\Desktop\Courses\ECC\hadoop-3.2.1\part1\reducer_chain1.py"
#step 2
hadoop jar C:\Users\Aditi\OneDrive\Desktop\Courses\ECC\hadoop-3.2.1\hadoop-3.2.1\share\hadoop\tools\lib\hadoop-streaming-3.2.1.jar -input \Aditi\part1\output_part1_step1 -output \Aditi\part1\output_part1_step2 -mapper "python C:\Users\Aditi\OneDrive\Desktop\Courses\ECC\hadoop-3.2.1\part1\mapper_chain2.py" -reducer "python C:\Users\Aditi\OneDrive\Desktop\Courses\ECC\hadoop-3.2.1\part1\reducer_chain2.py"
hdfs dfs -cat \Aditi\part1\output_part1_step2\part-00000