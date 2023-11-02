class Solution {
  public:
    int getAngle( int h, int m ) {
    const auto angle{ abs( 30 * h - 5.5 * m )};
    return min( angle, 360 - angle );
}
    
};