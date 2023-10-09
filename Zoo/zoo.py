"""The Zoo project: variables, data storage types such as lists, and working with while loops"""

print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")

camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that!"""

lion = r"""
The lion habitat...
                   ,   __, ,
   _.._         )\/(,-' (-' `.__
  /_   `-.      )'_      ` _  (_    _.---._
 // \     `-. ,'   `-.    _\`.  `.,'   ,--.\
// -.\       `        `.  \`.   `/   ,'   ||
|| _ `\_         ___    )  )     \  /,-'  ||
||  `---\      ,'__ \   `,' ,--.  \/---. //
 \\  .---`.   / /  | |      |,-.\ |`-._ //
  `..___.'|   \ |,-| |      |_  )||\___//
    `.____/    \\\O| |      \o)// |____/
         /      `---/        \-'  \
         |        ,'|,--._.--')    \
         \       /   `n     n'\    /
          `.   `<   .::`-,-'::.) ,'    
            `.   \-.____,^.   /,'
              `. ;`.,-V-.-.`v'
                \| \     ` \|\
                 ;  `-^---^-'/
                  `-.______,'
The lion is roaring!"""

deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""

goose = r"""
The goose habitat...
                                                       _...--.
                                       _____......----'     .'
                                 _..-''                   .'
                               .'                       ./
                       _.--._.'                       .' |
                    .-'                           .-.'  /
                  .'   _.-.                     .  \   '
                .'  .'   .'    _    .-.        / `./  :
              .'  .'   .'  .--' `.  |  \  |`. |     .'
           _.'  .'   .' `.'       `-'   \ / |.'   .'
        _.'  .-'   .'     `-.            `      .'
      .'   .'    .'          `-.._ _ _ _ .-.    :
     /    /o _.-'               .--'   .'   \   |
   .'-.__..-'                  /..    .`    / .'
 .'   . '                       /.'/.'     /  |
`---'                                   _.'   '
                                      /.'    .'
                                       /.'/.'
Beautiful!"""

bat = r"""
The bat habitat...
 /\                 /\
/ \'._   (\_/)   _.'/ \
|.''._'--(o.o)--'_.''.|
 \_ / `;=/ " \=;` \ _/
   `\__| \___/ |__/`
        \(_|_)/
         " ` "
It's doing fine."""

rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y    
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    print("Please enter the number of the habitat you would like to view:")
    user_input = input("> ")
    if user_input == 'exit':
        print("See you later!")
        break
    elif user_input.isdigit() and 0 <= int(user_input) <= 5:
        print(animals[int(user_input)])
        print("You've reached the end of the program.")
    else:
        print("Enter the correct number. Try from 0 to 5.")
