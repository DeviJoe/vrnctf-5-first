#define _GNU_SOURCE             /* See feature_test_macros(7) */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char flag[] = "oy4px_u0y3_pu4a_15_q4a63e0h5_4aq_ph73";

void foo();

char* rot13(char* s) {
    int c;
    char* t=s;
    while (c=*t) {
        if (c>='a' && c<='z') {
            c+=13;
            if (c>'z') c-=26;
            *t=c;
        }
        ++t;
    }
    return s
    ;
}

int main(int argc, char *argv[]) {

    printf("Hey, we're on a spaceship!\n"
           "Let's go on a journey through the endless space!\n");
    printf("                      .   *        .       .\n"
           "       *      -0-\n"
           "          .                .  *       - )-\n"
           "       .      *       o       .       *\n"
           " o                |\n"
           "           .     -O-\n"
           ".                 |        *      .     -0-\n"
           "       *  o     .    '       *      .        o\n"
           "              .         .        |      *\n"
           "   *             *              -O-          .\n"
           "         .             *         |     ,\n"
           "                .           o\n"
           "        .---.\n"
           "  =   _/__~0_\\_     .  *            o       '\n"
           " = = (_________)             .\n"
           "                 .                        *\n"
           "       *               - ) -       *\n");
    sleep(1);
    printf("                                                                    ..;===+.\n"
           "                                                                .:=iiiiii=+=\n"
           "                                                             .=i))=;::+)i=+,\n"
           "                                                          ,=i);)I)))I):=i=;\n"
           "                                                       .=i==))))ii)))I:i++\n"
           "                                                     +)+))iiiiiiii))I=i+:'\n"
           "                                .,:;;++++++;:,.       )iii+:::;iii))+i='\n"
           "                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'\n"
           "                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:\n"
           "                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+\n"
           "                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,\n"
           "                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+\n"
           "                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='\n"
           "                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`\n"
           "                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'\n"
           "                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,\n"
           "                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;\n"
           "                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;\n"
           "                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:\n"
           "                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=\n"
           "                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+\n"
           "                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'\n"
           "                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;\n"
           "              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;\n"
           "             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;\n"
           "           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,\n"
           "         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'\n"
           "       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+\n"
           "      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'\n"
           "     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'\n"
           "   .+=:))iiiiiiii)))+ii;\n"
           "  .+=;))iiiiii)));ii+\n"
           " .+=i:)))))))=+ii+\n"
           ".;==i+::::=)i=;\n"
           ",+==iiiiii+,\n"
           "`+=+++;`\n");
    sleep(1);
    printf("          .                            .                      .\n"
           "  .                  .             -)------+====+       .\n"
           "                           -)----====    ,'   ,'   .                 .\n"
           "              .                  `.  `.,;___,'                .\n"
           "                                   `, |____l_\\\n"
           "                    _,.....------c==]\"\"______ |,,,,,,.....____ _\n"
           "    .      .       \"-:______________  |____l_|]'''''''''''       .     .\n"
           "                                  ,'\"\",'.   `.\n"
           "         .                 -)-----====   `.   `.              LS\n"
           "                     .            -)-------+====+       .            .\n"
           "             .                               .\n");

    sleep(3);

    printf("     .kK;       '.                        .,,.                      .,l;            ..             'oKWWNx'      \n"
           "    'kc.     ...         .              ,:,.    . . ...... . ....    ..;oc;.      . ...               .,lONKx;.  \n"
           "   :x.    .;,                  .''  ':::..      .   .  ... .  . ..   ....;cc:;.       . ..                 ;xNNx,\n"
           "..o:    .:'                    .:d.'kO..do. c:  ::  c,  cc. ,,. .c  ;;,.cll'ldx:.l,       .                  .oNW\n"
           ".o:    :,           .             :o;'. ..                           .   ....cc :d.    . .....    .            .k\n"
           ",X.  ':             ......   .   lc;:..                                      .'l .l.    .......   ..             \n"
           "xk..:,    '   ..    ......     .llxd,..                                        .l  c'  ....'.. ..:..             \n"
           "0o,ol,...     ..'.. .....     .dOk:'....                                        .l  c.  .......';'.      ......  \n"
           "0o:xcllc:,.... .',,'.....     dxc;,.....                     .                   .l  o    ....,,..    ..;:c;'.   \n"
           "ldl,,cdOOOkxc'. ..','..    .:dc;'...           .             ..                   .c .:     ....   ..,cll:,.     \n"
           ".ko.'lxOKKXNKxc,.......  .:dld:,..           .,.             ',.                 ..', c          .':loc;..    '  \n"
           "..Ol;:ok0O0K00Oxo;'.....,l:,,k,..           .:o;.            'l;.                 ..,..,       ..,;;,..       .  \n"
           "  .o,'ck0K0O0OOK0d::,';:;'..kc....        ..:lll.            ,ll:.                 .,d.;     ...'...             \n"
           ".  .,,ck00K0000K0O00xc;;,'..k.,..        ..',,''..           ','''.                 .'d:     ...               .c\n"
           "......,,cxOkOKKK0KXo;odl:c:doc..        .';:c:;;,...  .      ',,,;;;..               ..:;...                 ':; \n"
           "...,c;'.,oolox0KKO:lKKOxllxk,.          ...,,;;;:'..  .......,,;:;;,...               ...c:..            .;::'   \n"
           "..'cxOkc,',:odkKd,xXKKXKxo;.           ''.:l:';,.... ........;,..;;,:d.....            ,'..,',;;;;;;;;;;;'       \n"
           "';'';;;codol,,,..:lool:'..            .:ol::clc'. .:..,'.....,...;c::;;:......      .  ,xoc;..'''.',;;,,,''',,;cl\n"
           "......';clcokx..llc:,'..              .cddoolc:;;:cll',c:....,lllcclooooo,......     ...lxlcl;'''',,,;:clllddxxxx\n"
           "  ....',,;:kk..lkOOkO00d.        .   .ccxddooooolloool:loc,..,looooooooddl:......    ..',oxoc:o;;::;'.....   . . \n"
           " .......':ko; ;lxkOOOk;         ...  .xkxkddddoooooooooooooc,.cooooddddxk0kd;.....   ....;kOdlck:lo,'''..........\n"
           "........,k,o..oodkOx;.         ....  ;dkOkOxxddddddddooooooooc;ldddddxkO00Okdl,....    ...'o0xxxx;lOllc;;'.......\n"
           "......,c0:c,..ddxl'            ......:odO0OOkxxxxxdddddddddddddodxxkkOOOOkxdxdoc.....    ...'o0Odl,oKxc::;...'...\n"
           "....',;Oc:;...,.              .......:ooxO000OxxxxxxxdolcloddxxxxxkO0Oxxxdoodxxxo'....      ...ck0.,OXxdoolc:oodd\n"
           "    ...                       .......cdddxO0KKK0OxodxxddddddddooOKK00Okdoooollolcc,......       .'..dOKddddolloo:\n"
           "     ..   .                   .......cdxdxOO0KKXXXc,,;:ccc:;,',kXXK0Oxxkxxxdolccccc,....;:'.       'c,,::cclodooc\n"
           "     ::...                    .......'odxkkO00KKXXo''''''''',,;OXXKOxxxkkOOkxlllclod;....;cc;.     .lOOl;'...',::\n"
           "...... ..                    .........,loxkO000KXXd,,,,'''',,,;kXXXKOkxxkkkkkkxddxdxd.....:ccc;.   ...:xxoc::,,'.\n"
           "..   .;.                .    ':........;dxkOO0KKKKl;,,'''''',,,lKXXK0OkxkkkkkOkkkxddd,.....cccc:.    . .,ol,,::co\n"
           "    '.                .,     ,c;........'lO00000ko::;,,''''''',;cdOK0OkkkkkOOkOOOkddd:.....;cccc;.       .:Od:,;c\n"
           "  .,                 .:.     ;ccc.........'okxololodolc;,,,,,,;;:cloxxxxkkkOOOOOkkkkx:......cccc:.       ',.oOo;;\n"
           " ,.                 'c'      ;cloc'..........;ldxddddoooollc;coodddddolc::cccllodxkkx'......:ccc:.        ,l.,OOd\n"
           ";.                 'c:.      ;c::oxo'   .......,:clloooooooo::ccc:;;;;;:ccloooddol:c;.......:ccc:.         ;o..lO\n"
           ".                 'cc:       ,;;dkkkxl. ....... ..,cccloooll:.,.:ccllooddddddddddd;.........:llc'           dl. ;\n"
           "                 ,cll:........,;oxxxxxx;      ',. ..;loollloo'..'cooooooodddddddl,..........clc,.           ,x;  \n"
           " .      .       'loool.........,cdxdddd.       ,l;  ..,loooool'   .';:clooolc;,.        ....dd'.            .O;. \n"
           " ..     ,.      :odlcl........ .'cddoo:         coc.  ..:oooooo:.                         .;x.      .       .0.. \n"
           " .;     ;'    ..'cllll:....... .'.,:lc.         ;ooc   ..:clooool;.                       .,.     .:.       .O.. \n"
           "  c.    ':.   ...'cloxxc......   .,,..          ;lol.    .clloooooo:.                     .     .;o:        lc.. \n"
           "   c.    ;:.  .....;ddxko.....    ..           .',;:.    .:clol:;'.                           .;xkc.       :o.', \n"
           "    d.   .:c. ......'ldxko....                 ,:c;.     .:cl:.,'                            'oxdc        ,d..., \n");
    printf("Oh no, it's a black hole chan!!!\n"
           "It's COMPRESSING us!!!!!\n"
           "We won't be able to deliver the flag to the base((\n");



    return 0;
}

void foo() {
    printf("Oh, we survived\n"
               "Here is your flag!\n"
               "%s", rot13(flag));
}

