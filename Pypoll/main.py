import os
import csv


election_data_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
output_file=os.path.join("Analysis", "election_analysis.txt")


votes=0
candidates_options=[]
candidates={}
winner=""
winning_count=0


with open(election_data_csv, encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    
    for row in reader:
        
        votes+=1
        candidate_name= row["Candidate"]
        
        
        if candidate_name not in candidates_options:
           candidates_options.append(candidate_name)
           candidates[candidate_name]=0
        
        candidates[candidate_name]=candidates[candidate_name]+1
           
    for candidate in candidates:
        candidate_votes=candidates.get(candidate)
        vote_percentage=(float(candidate_votes)/float(votes))*100
        
        if (candidate_votes > winning_count):
            winning_count=candidate_votes
            winner=candidate
 
            
    
       
          
        print("Election Results")                                      
        print("----------------------------\n")                                                   
        print(f"Total Votes:  {votes}\n")
        print("----------------------------\n")
        print(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes})\n")
    print("-------------------------------")
    print(f"Winner:   {winner}")
    print("-------------------------------")
    
with open(output_file, "w") as txt_file:
                
        txt_file.write("Election Results\n") 
        txt_file.write("----------------------------\n") 
        txt_file.write(f"Total Votes:  {votes}\n") 
        txt_file.write("----------------------------\n")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes})\n") 
        txt_file.write("----------------------------\n")
        txt_file.write(f"Winner:   {winner}\n")  
        txt_file.write("----------------------------\n")


            
        
        
    
    
    
    
                                        

    
