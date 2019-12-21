let sort = z => z.replace(/\s+/g, "").toLowerCase().split("").sort().join();

let anagram = (x, y) => (sort(x) === sort(y));

anagram("the eyes", "they see");
