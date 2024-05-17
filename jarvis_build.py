from Constants import OS, BuildPlatforms
from SkypeService import SkypeService
from DiawiService import DiawiService
from android_build import android_build
from user_input_handler import HandleUserInput
from ios_build import ios_build

if __name__ == "__main__":
    skypeService = SkypeService()
    diawiService = DiawiService()

    print("\n")
    print("""
                     .B@@@@@@!  ?###&&&@@@@   . ^5GB#&&&@@@@@@&B7 !@@@@@@7  J@@@@@&:JGGB#&G    :!YPB&&@@@&#G 
                     !@@@@@@P. ^&@@@@@@@@@@     J@@@@@@@@@@@@@@@@ !@@@@@@^ :&@@@@@7:@@@@@@? :?G&@@@@@@@@@@@@&
                     G@@@@@@~  P@@@@@J#@@@@     G@@@@@#JJJY5#@@@@ 7@@@@@#. ?@@@@@B.J@@@@@#.7#@@@@@@GJ7P@@@@@@
                    ^@@@@@@P  ?@@@@@P:&@@@@    ^@@@@@@J    :G@@@# J@@@@@P .#@@@@@~ B@@@@@Y?@@@@@@@J   :##G5J7
                    Y@@@@@@~ :&@@@@@^~@@@@@    J@@@@@&: .~5&@@@B^ 5@@@@@? 7@@@@@P !@@@@@&^B@@@@@@@@     
                   .#@@@@@G  5@@@@@5 ?@@@@@   .#@@@@@B?P#@@@@@5:  G@@@@@~ G@@@@@^ P@@@@@P ?@@@@@@@@@@
                   7@@@@@@! !@@@@@&^ 5@@@@@   7@@@@@@@@@@@@#Y^    #@@@@&:~@@@@@5 ^@@@@@@~   P&@@@@@@@@@B     
                   G@@@@@B .#@@@@@J  B@@@@@   P@@@@@@@@@@@J       &@@@@B P@@@@&: Y@@@@@B     ^?G@@@@@@@@@
                  ^&@@@@@? Y@@@@@&7~7&@@@@@  :&@@@@@?P@@@@#~      @@@@@5^@@@@@J :&@@@@@?        ~J#@@@@@@#   
                  Y@@@@@# ~@@@@@@@@@@@@@@@@  J@@@@@#.~@@@@@#^     @@@@@7Y@@@@#. ?@@@@@#:  ^^      ^&@@@@@@
              JJ!J@@@@@@7 B@@@@@@BBB#@@@@@@  #@@@@@Y  P@@@@@#:    @@@@@P&@@@@? .B@@@@@Y  !&&57^   Y@@@@@@G    
             Y@@@@@@@@@P Y@@@@@@?   Y@@@@@@ !@@@@@@~  :&@@@@@B:   @@@@@@@@@@B. 7@@@@@@~ 7@@@@@@&&@@@@@@@#
            Y@@@@@@@@@P ~@@@@@@B    G@@@@@@ P@@@@@B   J@@@@@@5   t@@@@@@@@@? .B@@@@@G  #@@@@@@@@@@@@@&Y 
            JG&@@@@&B?  G&##BGG~   :#@&#BBP &&#BP5~    .GB5J!^:  @@@&&#BBG5. 7@@&&##7   7P#@@@@@@&B57   
    """)

    result = HandleUserInput(skypeService.getContacts())

    directory_path = result[0]
    platform = result[1]
    build_type = result[2]
    sendToWhom = result[3:]

    match platform:
        case BuildPlatforms.Android:
            android_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
        case BuildPlatforms.IOS:
            ios_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
        case BuildPlatforms.Both:
            android_build(directory_path, build_type, sendToWhom, skypeService, diawiService)
            ios_build(directory_path, build_type, sendToWhom, skypeService, diawiService)


