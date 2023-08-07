import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    val n = sc.nextInt()

    for (i in 1 .. n) {
        for (j in 0 until i){
            print("*")
        }
        println()
    }


}