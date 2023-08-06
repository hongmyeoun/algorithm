import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    var h = sc.nextInt()
    var m = sc.nextInt()

    //h m - 45
    //if m - 45 < 0
    //h - 1, m + 60 - 45
    //if h < 0
    //h + 24 - 1
    m -= 45
    if (m < 0) {
        h -= 1
        m += 60
        if (h < 0) {
            h += 24
        }
    }
    println("$h $m")
}