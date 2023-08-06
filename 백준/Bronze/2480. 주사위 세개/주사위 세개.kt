import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    val a = sc.nextInt()
    val b = sc.nextInt()
    val c = sc.nextInt()
    var price = 0

    //두개가 같을 경우
    //a,b or b,c or c,a
    //다 다를때 비교
    //if a>b 일때
    //if b>c 이면 가장큰수 a
    //else if b<c 이면
    //if a>c 일때 가장큰수 a
    //else if a<c 가장큰수 c
    if (a==b&&b==c){
        price = 10000+a*1000
    }else if (a==b||b==c||c==a){
        if (a==b){
            price = 1000+a*100
        }
        if (b==c){
            price = 1000+b*100
        }
        if (c==a){
            price = 1000+c*100
        }
    }else{
        if (a>b){
            if (b>c){
                price=a*100
            }else if(b<c){
                if (a>c){
                    price=a*100
                }else if(a<c){
                    price=c*100
                }
            }
        }else if (a<b){
            if (b>c){
                price=b*100
            }else if (b<c){
                price=c*100
            }
        }
    }
    println(price)
}