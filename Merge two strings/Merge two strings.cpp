string merge (string S1, string S2)
{
    int n=min(S1.length(),S2.length());
    string s="";
    for(int i=0;i<n;i++){
        s=s+S1[i]+S2[i];
    }
    if(S1.length()>S2.length()){
        for(int i=n;i<S1.length();i++){
            s+=S1[i];
        }
    }else{
        for(int i=n;i<S2.length();i++){
            s+=S2[i];
        }
    }
    return s;
}