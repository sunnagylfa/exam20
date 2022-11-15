def main():
    cand_vote_list=[]
    candidate_and_votes=input("Candidate and votes: ")
    no_entry=False
    if candidate_and_votes=="":
        print("Total no. of votes: 0")
        no_entry=True
    while candidate_and_votes!="":
    #muna að setja allt sem ég vil gera í try ef ég er að nota try
        try:
            cand_list=candidate_and_votes.lower().strip().split(" ")
            if len(cand_list)>1:
                cand_list[1]=int(cand_list[1])
                cand_list=readinfo(cand_list, cand_vote_list)
            else:
                raise ValueError
            
        except ValueError:
            print("Invalid no. of votes!")
        candidate_and_votes=input("Candidate and votes: ")
    #passa að ég má ekki gera þetta ef ég fór aldrei í gegnum whiele
    if not no_entry:  
        final_list=check_for_duplicates(cand_list) 
        printvotes(final_list)


def readinfo(cand_list, cand_vote_list):

    cand_vote_list.append(cand_list)
   
    return cand_vote_list   
    

def check_for_duplicates(cand_vote_list):
    """function to check if candidates appear more than once and
    fix list accordingly by adding total votes"""
    name_list=[]
    cand_list=[]
    dupl_list=[]
 
    for item in cand_vote_list:
        if item[0] not in name_list:
            name_list.append(item[0])
            cand_list.append(item)
        else:
            dupl_list.append(item)
    for dupl in dupl_list:
        for item in cand_list:
            if item[0]==dupl[0]:
                
                item[1]+=dupl[1]
    cand_list=sorted(cand_list, 
       key=lambda x: x[0])
    return cand_list
def printvotes(cand_list):
    total_votes=0
    for candidate in cand_list:
        print(f"{candidate[0]}: {candidate[1]}")
        total_votes+=candidate[1]
    print(f"Total no. of votes: {total_votes}")

    

if __name__ == "__main__":
    main()