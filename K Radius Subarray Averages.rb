def get_averages(nums, k)
    res = []
    len = nums.length()
    div = k*2+1
    sum = 0
    ins = 0
    inp = 0
    if k == 0 then
        return nums
    end
    if len >= k+k then
        for i in k..k+k-1
            ins = ins + nums[i]
        end
    end
    for n in 0..len-1 do
        if n<k then
            res.push(-1)
            sum = sum + nums[n]
        elsif n>=k && n<len-k
            ins = ins - nums[n]
            ins = ins + nums[n+k]
            inp = (ins + sum + nums[n])/div
            inp = inp.floor
            res.push(inp)
            sum = sum + nums[n]
            sum = sum - nums[n-k]
        else
            res.push(-1)
        end
    end
    return res
end


puts get_averages([7,4,3,9,1,8,5,2,6],3)