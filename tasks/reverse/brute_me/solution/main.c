#include <stdio.h>
#include <string.h>
#include "openssl/md5.h"
#include "tigress/3.1//tigress.h"

void compute_md5(char *str, unsigned char digest[16]) {
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, str, strlen(str));
    MD5_Final(digest, &ctx);
}

int main(void) {
    setbuf(stdout, NULL);
    char sug[256];
    printf("Write your flag: ");
    scanf("%s", sug);

    const char *he4llo3 = "3a0482bcc009def3da6fa5c41f7fd41c";
    const char *hel4lo3 = "efcf186eeb21cf1225a045025a94c33f";
    const char *hel44lo3 = "a594f01cf778c51a7a21f4bff0195136";
    const char *he44llo3 = "33ac7db4d0add55054cd124718bf8e46";
    const char *hell66o3 = "9aab70ef1fa79786417773465ca0090";
    const char *hell666o3 = "c80b938c721e006a7a497b8e61f83b76";
    const char *hel6lo3 = "3dfd23f6833d6e45a57af5d459e9f297";
    const char *hel66lo3 = "413005a41f001c88b9ec49988351382";
    const char *h6ell66o3 = "aa95e4595d4977129837f181799edbba";
    const char *helklo3 = "ef409b404b9e0fe76de82d67196ba3aa";
    const char *hell6k66o3 = "f3d029c7aa4b7a0f58e0a098dd9a2cb0";
    const char *helkklo3 = "de279f35639653b50fe938953e733f49";
    const char *helkkklo3 = "e002cd99b0472aa2bb1fb4e9b3eafd8e";
    const char *helkl77o3 = "bf18d90cfc404b98d71e728922a54c3a";
    const char *helk777lo3 = "6542d9b44b28bf5b3aeb782b043c2f92";
    const char *hell7777o3 = "f5e8d8951674289aba9600cb7d04355d";
    const char *hell77777o3 = "f6b05eb2e5b5788e553396520511f545";
    const char *hell777777o3 = "c8d22264d2df80e388ffbc515a2f3566";
    const char *hello3111111 = "4c8b8dd1dd0cb3f54956599df6e84490";
    const char *hello31 = "1478b4cb65454d311f15c681656904f8";
    const char *hello311 = "3587145c962ec7b45e629f7e886b2550";
    const char *hello3111 = "0bb92f6da1f72d543790a0e1dadb39ef";
    const char *hello31111 = "6d13cea5cb13724bf1f60e7afa451097";
    const char *hello311111 = "306f06e87c61232b0e2671d38ceb935c";
    const char *hello31111111 = "78bcc4fd1c279ab2d197719b5b4d0a19";
    const char *hello3111111111 = "731ca33cd1c7171c768e61f451b8ea3f";
    const char *hello31111111111 = "36698b4ef9db9c376b1c28c7671d6ab2";
    const char *hello32 = "ff6c5868e137f934bd21bd2cbbb9e562";
    const char *hello322 = "8faa7c71a6881afaa305f60aedb681e3";
    const char *hello3222 = "b68c9466ba1fb6720315695d4ad97ada";
    const char *hello32222 = "1ed661b4118ec1e9612cae99f1fecf7f";
    const char *hello322222 = "f12d3813403f2343188ec286b83b24af";
    const char *hello3222222 = "cdd89b22c1a21eb4dae8f8b6d4e728ab";
    const char *hello32222222 = "0281294c160a9fd23898792082395ee4";
    const char *hello322222222 = "c3f80538e5413e09fe798ced5689f612";
    const char *hello3222222222 = "6f16a98ac7eb7499bc2b73d2ad51d8dd";
    const char *gggg = "b711766a6321b9eaf58e363cec5c2df2";
    const char *hello33 = "94a08cc6f464872606404f739282b7fc";
    const char *hello3333 = "b8af6f1e7eae773c8c3c1fa207ec1da8";
    const char *hello333 = "ebbfee829c799edba1da11c694484cfa";
    const char *hello33333 = "2aea1089c2d053da596cc167e968b0a2";
    const char *hello333333 = "851411bfb1673d0d13911e233772feef";
    const char *hello33333333 = "079ec8f55501124e2cb51ca81b51d0b4";
    const char *hello3333333 = "c62451655413864e2411226b1d99b203";
    const char *hello4444443 = "24f9a188e3fb663b5aff868b9e44f384";
    const char *hello34 = "5dd6f5e9d32a9d921b5173c201f7d5e4";
    const char *hello344 = "6d0e9359670cc3fed303c09fddc034bf";
    const char *hello3444 = "5c7a198c5987110d11a13c4e21ba8b0f";
    const char *hello34444 = "ceea841a1e052f0cafcf396080560668";
    const char *hello344444 = "fe35ba8559bf11055a3bdabcb3ab9d17";
    const char *hello = "93eceba540270cb2bff64be5519940f7";
    const char *h1ello322222222 = "57c8b3127faa496e0976c1893f0adce7";
    const char *he1llo322222222 = "c838fc5badadd638d48539339213e077";
    const char *hel1lo322222222 = "be26adae93760370042ad60ba3595ff9";
    const char *hell1o322222222 = "feeb8141a6c90f73fbffc1fb59d304d6";
    const char *hello1322222222 = "e5d98bf599997b9ffdca45799e1c896b";
    const char *hello3122222222 = "5d65c79c728de7c4971b45708585acb8";
    const char *hello3212222222 = "88a568075c1918b5369a3482616c0819";
    const char *hello3221222222 = "6025ffa095367d9be7a356299aaa2dd4";
    const char *hello3222122222 = "a63d762a79d9bb6aeb096b4aa215c1dc";
    const char *hello3222212222 = "2e60cac9b7c7384fbe42dd1e412d18fd";
    const char *hello3222221222 = "d3485ebdb0d0c0747d01265dacb95c8f";
    const char *hello3222222122 = "9ceb6e155ac3c35825a625c785cf6727";
    const char *hello3222222212 = "d1a17bf59cf84a480c816c859a353849";
    const char *h2ello322222222 = "5c005815bcbb2f0a86aa6a4f7fabe4e1";
    const char *he2llo322222222 = "676e0641494396316c9e5da9ddee242c";
    const char *hel2lo322222222 = "61d3a81d85225b0b4fc5a2abab316d94";
    const char *hell2o322222222 = "bd34652982b53aff0d43efac1128d9e2";
    const char *hello2322222222 = "ae7844cbc7c27b71676fa5a764846239";
    const char *hello33222222222 = "0e5e7ff71bd98dcd8863fc8c32743bee";
    const char *hello32322222222 = "043f0119bce5e32a2a1f9cfea057947a";
    const char *hello32232222222 = "b23b957d2d9e92fddc0bd2d72b0ecf5d";
    const char *hello32223222222 = "ade192392f94f9abb91b5652eb699eb1";
    const char *hello32222322222 = "8dfab9deafb4aca3dd9f1c30d3cd1910";
    const char *hello32222232222 = "a5b6bf4e1d672f2d12ef004d4ff63b83";
    const char *hello322222233222 = "d89ec412bf27c255cdaccf0c370cf8b0";
    const char *hello32222222232 = "81ccfebd0a907590ff4a7c310cf24f4d";
    const char *hello32222222223 = "a53da312feae0f3f8f61cde485be6085";
    const char *h4ello322222222 = "1af209d023c4478a6b03dc8324c1bab9";
    const char *he4llo322222222 = "b24b50ff280678d415764b57d1a9f6d9";
    const char *hel4lo322222222 = "66e6517da2005bd986fb95107dc2ceec";
    const char *hell4o322222222 = "977587e8c5c2d6e38c2f94ce357828ef";
    const char *hello4322222222 = "608a0d4a1ee9ee1d469a0feaba423aee";
    const char *hello3422222222 = "aab9e761cc2fcc8c33efcc58a4467301";
    const char *hello3242222222 = "08e71e84e3b807c8ee22642f7eb44d81";
    const char *hello3224222222 = "e5b80f472ffff57d04c3748e978066f5";
    const char *hello3222422222 = "b3b5cdc64e87b74e2fa922218d5978f8";
    const char *hello3222242222 = "1212a1386b9f812a6ba56f0680571a0c";
    const char *hello3222224222 = "9524c7296a4cee2a237f170d364bc75a";
    const char *hello3222222422 = "ee478e44128f048d13734314564e9b81";
    const char *hello3222222242 = "625092bdfb37dcd9c9394d366e73f42f";
    const char *hello3222222224 = "1d523e898aa830b6207e8cdd5c69e247";
    const char *h5ello322222222 = "932c14f9a4b64f4c20531eeb15ae375b";
    const char *he5llo322222222 = "da4ab73aae6509c266123f93d5678526";
    const char *hel5lo322222222 = "2e29a9b22777a5f59a55055f003f63ce";
    const char *hell5o322222222 = "65f4a4e97aa85adbf09579d10417f64b";
    const char *hello5322222222 = "b8aa88d14659cfafba1ada50844c825a";
    const char *hello3522222222 = "75626f0127785ff5e69a031c131af7a1";
    const char *hello3252222222 = "b33946c7e0fbda4815ed5d64e061f294";
    const char *hello3225222222 = "35fd09ca3adc4ff64951dad3f82a9990";
    const char *hello3222522222 = "71b672652a7d7ba8ec017068c167584f";
    unsigned char digest[156];
    char buf[sizeof digest * 2 + 1];
    compute_md5(sug, digest);
    for (int i = 0, j = 0; i < 16; i++, j+=2)
        sprintf(buf+j, "%02x", digest[i]);
    buf[sizeof digest * 2] = 0;
    if (strncmp(hello, buf, 32) == 0) {
        printf("Correct!");
    } else {
        printf("No.");
    }

    return 0;
}