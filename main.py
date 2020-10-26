def hello():
  print('This is a sample python program');
  return 'ok';

def test_hello():
  assert hello() == 'ok';
  
if __name__ == '__main__':
  hello();
