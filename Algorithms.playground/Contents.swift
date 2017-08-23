import UIKit

var custom = [100,4,6,3,2,10,7]

func insertionSort(arr: [Int]) -> [Int] {
    var newArr = arr
    var next = 0
    var previous = 0
    for i in 1..<arr.count {
        var y = i
        next = newArr[y]
        previous = newArr[y-1]
        while y > 0 && next < previous {
            swap(&newArr[y], &newArr[y-1])
            print(newArr, "next: \(next), previous: \(previous)")
            y -= 1
            if y == 0 {
                
            }else {
                next = newArr[y]
                previous = newArr[y-1]
            }
        }
    }
    return newArr
}

insertionSort(arr: custom)

func insertionSort2(_ array: [[String: String]]) -> [[String: String]] {
    var a = array
    var updateid = 0
    var updateIdinit = 0
    
    for x in 1..<a.count {
        var y = x
        let kee = a[y].keys.first!
        let kee2 = a[y-1].keys.first!
        let index1 = kee.index(kee.startIndex, offsetBy: 4)
        let index2 = kee2.index(kee2.startIndex, offsetBy: 4)
        updateid = Int(kee.substring(from: index1))!
        updateIdinit = Int(kee2.substring(from: index2))!
        print("before",updateid, updateIdinit)
        
        while y > 0 && updateid < updateIdinit {
            swap(&a[y], &a[y-1])
            y -= 1
            if y == 0 {
                
            } else {
                let kee = a[y].keys.first!
                let kee2 = a[y-1].keys.first!
                let index1 = kee.index(kee.startIndex, offsetBy: 4)
                let index2 = kee2.index(kee2.startIndex, offsetBy: 4)
                updateid = Int(kee.substring(from: index1))!
                updateIdinit = Int(kee2.substring(from: index2))!
                print(a)
            }
        }
    }
    return a
}







