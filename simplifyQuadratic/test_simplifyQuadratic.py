from simplifyQuadratic import simplifyQuadratic

def test_coefficient_zero():
    assert simplifyQuadratic('16x^2+10x') == '8x^2+5x'
    assert simplifyQuadratic('21x^2+7x') == '3x^2+x'
    assert simplifyQuadratic('10x^2+5x+3') == '10x^2+5x+3'
    assert simplifyQuadratic('39x^2+3') == '13x^2+1'
    assert simplifyQuadratic('3x^2+21') == 'x^2+7'
    assert simplifyQuadratic('16x^2+32x') == 'x^2+2x'
    assert simplifyQuadratic('16x+8') == 'ERROR: No x^2 term'
    assert simplifyQuadratic('16x-8') == 'ERROR: No x^2 term'

def test_negative_coefficient():
    assert simplifyQuadratic('-16x^2+8x-24') == '2x^2-x+3'
    assert simplifyQuadratic('-3x^2+9x-12') == 'x^2-3x+4'
    assert simplifyQuadratic('-1x^2+3x-2') == 'x^2-3x+2'
    assert simplifyQuadratic('-3x^2-3x+3') == 'x^2+x-1'
    assert simplifyQuadratic('3x^2-x') == '3x^2-x'
    assert simplifyQuadratic('-3x^2+9') == 'x^2-3'
    assert simplifyQuadratic('-2x^2-2x-2') == 'x^2+x+1'
    assert simplifyQuadratic('9x^2-6') == '3x^2-2'

def test_decimal_coefficient():
    assert simplifyQuadratic('6.6x^2+4.4x-2.2') == '3x^2+2x-1'
    assert simplifyQuadratic('6.6x^2-2.2') == '3x^2-1'
    assert simplifyQuadratic('0.05x^2+0.3x-10') == 'x^2+6x-200'
    assert simplifyQuadratic('-0.6 x^2+0.03x-9') == '20x^2-x+300'
    assert simplifyQuadratic('0.01x^2+0.5x-0.7') == 'x^2+50x-70'
    assert simplifyQuadratic('2x^2+0.4x+0.8') == '5x^2+x+2'
    assert simplifyQuadratic('0.003x^2-0.2x+2.02') == '3x^2-200x+2020'
    assert simplifyQuadratic('0.015x^2+3x-1') == '3x^2+600x-200'