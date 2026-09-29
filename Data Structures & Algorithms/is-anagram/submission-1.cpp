class Solution {
public:
    bool isAnagram(string s, string t) {
        multiset<char> seen_s;
        multiset<char> seen_t;
        for(char alpha_s : s)
        {
            seen_s.insert(alpha_s);
        }

        for(char alpha_t : t)
        {
            seen_t.insert(alpha_t);
        }
        if(seen_s == seen_t)
            return true;
        return false;
    }
};
