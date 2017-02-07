import java.util.SortedSet;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Iterator;
import java.util.TreeSet;

public class PipeAndFilter {
	private SortedSet<String> words = new TreeSet<>();
	public void readTextFile(String location) throws FileNotFoundException {
		File file = new File(location);
		Scanner inputFile = new Scanner(file);
		while(inputFile.hasNext()) {
			String word = inputFile.next();
			word = word.replaceAll("[,!.]", "");
			words.add(word.toLowerCase());
		}
		inputFile.close();
		Iterator it = words.iterator();
		while(it.hasNext()) {
			Object element = it.next();
			System.out.println(element.toString());	
		}
	}
	public void displaySet(SortedSet<String> words) {
		return;
	}
	public static void main(String []args) throws FileNotFoundException {
	   String location = "/home/arturo/Documents/Github/General/Software Architecture/HW1/pftest.txt";
	   PipeAndFilter instance = new PipeAndFilter();
	   instance.readTextFile(location);
   }
} 