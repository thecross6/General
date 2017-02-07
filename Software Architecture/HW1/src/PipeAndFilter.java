import java.util.SortedSet;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Iterator;
import java.util.TreeSet;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class PipeAndFilter {
	private SortedSet<String> words = new TreeSet<>();
	public SortedSet<String> readTextFile(String location) throws FileNotFoundException {
		File file = new File(location);
		Scanner inputFile = new Scanner(file);
		while(inputFile.hasNext()) {
			String word = inputFile.next();
			word = word.replaceAll("[,!.]", "");
			words.add(word.toLowerCase());
		}
		inputFile.close();
		return words;
	}
	public void writeText(SortedSet<String> words) throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter("Output.txt", false));
		Iterator it = words.iterator();
		while(it.hasNext()) {
			Object element = it.next();
			writer.write(element.toString());
			writer.newLine();
			System.out.println(element.toString());
		}
		writer.close();
	}
	public static void main(String []args) throws IOException {
	   String location = "C:\\Users\\Arturo Laguna\\Documents\\GitHub\\General\\Software Architecture\\HW1\\pftest.txt";
	   // C:\\Users\\Arturo Laguna\\Documents\\GitHub\\General\\Software Architecture\\HW1\\pftest.txt
	   // /home/arturo/Documents/Github/General/Software Architecture/HW1/pftest.txt 
	   PipeAndFilter instance = new PipeAndFilter();
	   instance.writeText(instance.readTextFile(location));
   }
} 