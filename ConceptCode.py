function readLine() {
     read string
    #parse/validate string
    switch/case $line in
        exit) return false
        ;;
        height)
            setHeight()
            return true;

}

function main() {
    while readLine() do {
      printStaircase
    }
}
