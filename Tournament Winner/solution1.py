def tournamentWinner(competitions, results):
         get={}
         for i in range(0,len(results)):
             if results[i] == 0:
                 if competitions[i][1] in get:
                    get[competitions[i][1]]= get[competitions[i][1]] + 1
                 else:
                    get[competitions[i][1]]=1
                              
             else:
                if competitions[i][0] in get:
                    get[competitions[i][0]]= get[competitions[i][0]] + 1
                else:
                    get[competitions[i][0]]=1

         winningTeam = max(get, key=get.get)
         return winningTeam
