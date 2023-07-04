def single_number(nums)
    has = {}
    nums.each do |n|
        if has[n] then
            has[n] = has[n] + 1
        else
            has[n] = 1
        end
    end
    a = []
    n = 0
    has.keys.each do |k|
        if has[k]==1 then
             a.push(k)
             n = n+1
             if n==2 then
                return a
                break
             end
        end
    end
end

puts single_number([1,1,3,2,6,6])