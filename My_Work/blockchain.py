import hashlib
class Block:
	def __init__(self,no,nonce,data,hashcode,prev):
		self.no=0
		self.nonce=nonce
		self.data=data
		self.hashcode=hashcode
		self.prev=prev
	
	def getStringVal(self):
		return self.no,self.nonce,self.data,self.hashcode,self.prev

class BlockChain:
	def __init__(self):
		self.chain=[]
		self.prefix="0000"
		
	def addNewBlock(self,data):
		no=len(self.chain)
		nonce=0
		
		if(len(self.chain)==0):
			prev="0"
		else:
			prev = self.chain[-1].hashcode
		
		myhash=hashlib.sha256(str(data).encode('utf-8')).hexdigest()
		block=Block(no,nonce,data,myhash,prev)
		
		self.chain.append(block)
	
	def PrintBlockChain(self):
		chainDict={}
		for i in range(len(self.chain)):
			chainDict[i]=self.chain[i].getStringVal()
		print(chainDict)
	
	def mineChain(self):
		brokenLink = self.checkIfBroken()
		
		if(brokenLink != None):
			for block in self.chain[brokenLink.no:]:
				print("Mining Block--> ",block.getStringVal())
				self.mineBlock(block)
	
	def mineBlock(self,block):
		nonce=0
		myhash=hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
		while(myHash[0:4]!=self.prefix):
			myhash=hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
			nonce=nonce+1
		self.chain[block.no].hashcode = myHash
		self.chain[block.no].nonce = nonce
		if(block.no < len(self.chain)-1):
			self.chain[block.no+1].prev=myHash
			
	def checkIfBroken(self):
		for n in range(len(self.chain)):
			if(self.chain[n].hashcode[0:4]!=self.prefix):
				self.chain[n]
	
	def changeData(self,no,data):
		self.chain[no].data=data
		self.chain[no].hashcode=hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
