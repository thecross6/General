import java.util.Set;
import java.io.File;
import java.util.Scanner;

public class PipeAndFilter {
	private Set<String> words;
	public void readTextFile(String location) {
		File file = new File(location);
		Scanner inputFile = new Scanner(file);
		while(inputFile.hasNext()) {
			String word = inputFile.nextLine();
			System.out.println(word);
		}
		
		inputFile.close();
	}
	public void displaySet(Set<String> words) {
		return;
	}
	public static void main(String []args) {
	   String location = "/home/arturo/Documents/Github/General/Software Architecture/Hw1/pftest.txt";
	   PipeAndFilter aclass = new PipeAndFilter();
	   aclass.readTextFile(location);
   }
} 