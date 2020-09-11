from xml.dom import  minidom

class redxml():
  def  xml(self,filename,y,z):
       '''
       x:xml文件路径
       y，z:xml的标签名
       '''
       root = minidom.parse(filename)
       firstnode = root.getElementsByTagName(y)[0]
       secondnode = firstnode.getElementsByTagName(z)[0].firstChild.data
       return secondnode